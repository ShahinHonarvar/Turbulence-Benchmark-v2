def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 419):
        substr = s[i:i + 420]
        if len(substr) == 420 and substr.isalpha() and (substr == substr[::-1]):
            palindromes.add(substr)
    return palindromes