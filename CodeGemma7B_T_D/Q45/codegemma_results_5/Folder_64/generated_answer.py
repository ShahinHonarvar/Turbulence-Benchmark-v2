def palindromes_between_indices(word):
    set_of_palindromes = set()
    for each_permutation in itertools.permutations(word[4:10]):
        if ''.join(each_permutation).lower() not in set_of_palindromes and ''.join(each_permutation).lower() == ''.join(each_permutation).lower()[::-1]:
            set_of_palindromes.add(''.join(each_permutation).lower())
    return set_of_palindromes