def palindrome_of_length_at_least_n(s):
    s = ''.join((char.lower() for char in s if char.isalpha()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n):
            substr = s[i:j + 1]
            if len(substr) >= 3 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes