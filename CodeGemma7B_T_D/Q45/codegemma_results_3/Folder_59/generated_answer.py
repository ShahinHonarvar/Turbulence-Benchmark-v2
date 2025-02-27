def palindromes_between_indices(string):
    palindromes = set()
    for letter in string[8:10]:
        if letter.isalpha():
            if letter.islower():
                for permutation in permutations(string):
                    if permutation.startswith(letter):
                        palindromes.add(''.join(permutation))
            else:
                for permutation in permutations(string):
                    if permutation.lower().startswith(letter):
                        palindromes.add(''.join(permutation))
    return palindromes