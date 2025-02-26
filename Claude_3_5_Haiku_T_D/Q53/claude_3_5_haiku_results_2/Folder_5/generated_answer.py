def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j + 1]
            if len(substr) >= 46 and substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes