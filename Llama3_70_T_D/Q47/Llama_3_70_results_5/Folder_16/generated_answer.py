def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[15:87]
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(51, 61):
            substr = s[i:i + j]
            if len(substr) == j and substr.isalpha() and (substr == substr[::-1]):
                palindrome_set.add(substr)
    return palindrome_set