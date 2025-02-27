def palindrome_of_length_n(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    n = 100
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(26):
            palindrome = letters[j] * (n // 2 - 1) + s[i + n // 2 - 1 - j] + letters[j] * (n // 2)
            if n % 2 == 1 and i + n // 2 - 1 - j == i + n // 2:
                continue
            if palindrome in s and s.find(palindrome, i, i + n) != -1:
                palindromes.add(palindrome)
    return palindromes