def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 288):
        substr = s[start:start + 289]
        if len(substr) == 289 and substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes