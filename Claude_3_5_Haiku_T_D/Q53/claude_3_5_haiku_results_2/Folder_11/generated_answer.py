def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 54
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(substr) >= n and substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes