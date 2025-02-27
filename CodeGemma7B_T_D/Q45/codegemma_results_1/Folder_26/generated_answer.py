def palindromes_between_indices(str_):
    set_of_palindromes = set()
    str_lower = str_.lower()
    letters_in_range = str_lower[4:7]
    for permutation in itertools.permutations(letters_in_range):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3:
            set_of_palindromes.add(palindrome)
    return set_of_palindromes