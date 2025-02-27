def palindromes_between_indices(s):
    n = len(s)
    palindromes_set = set()
    palindromes_between = s[1:8]
    for p in itertools.permutations(palindromes_between):
        palindrome_str = ''.join(p)
        if len(palindrome_str) >= 5 and palindrome_str == palindrome_str[::-1]:
            palindromes_set.add(palindrome_str.lower())
    return palindromes_set