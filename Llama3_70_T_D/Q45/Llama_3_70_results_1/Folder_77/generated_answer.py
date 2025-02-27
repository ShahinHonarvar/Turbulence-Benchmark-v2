def palindromes_between_indices(s):
    s = s[4:7].lower()
    s_set = set(s)
    palindromes = set()
    for c1 in s_set:
        for c2 in s_set:
            if c1 != c2:
                palindrome = c1 + c2 + c2 + c1
                palindromes.add(palindrome)
    return palindromes