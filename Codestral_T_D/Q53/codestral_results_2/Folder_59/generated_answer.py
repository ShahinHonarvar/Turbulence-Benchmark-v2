def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha() and (len(substr) >= 20):
                palindromes.add(substr)
    return palindromes