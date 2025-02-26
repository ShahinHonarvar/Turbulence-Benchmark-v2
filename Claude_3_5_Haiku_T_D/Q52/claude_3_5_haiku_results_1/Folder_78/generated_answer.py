def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    target_length = 48
    for start in range(n - target_length + 1):
        substr = s[start:start + target_length]
        if len(substr) == target_length and substr.isalpha() and (substr == substr[::-1]):
            palindromes.add(substr)
    return palindromes