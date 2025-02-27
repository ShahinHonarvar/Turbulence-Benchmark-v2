def palindromes_between_indices(word):
    letters = list(word[2:7].lower())
    palindromes = set()
    seen = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for permutation in itertools.permutations(letters[i:j + 1]):
                palindrome = ''.join(permutation)
                if palindrome not in seen and palindrome not in palindromes and (len(palindrome) >= 4):
                    palindromes.add(palindrome)
                    seen.add(palindrome)
    return palindromes