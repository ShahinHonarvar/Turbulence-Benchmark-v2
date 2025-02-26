def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 391):
        substr = s[start:start + 392]
        if len(substr) == 392 and substr.isalpha() and (substr == substr[::-1]):
            palindromes.add(substr)
    return palindromes