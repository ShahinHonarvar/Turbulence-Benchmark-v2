def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 55):
        for j in range(i + 56, n + 1):
            substr = s[i:j]
            if len(substr) == 56 and substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes