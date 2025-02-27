def palindromes_between_indices(s):
    letters = set(s[4:10].lower())
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes