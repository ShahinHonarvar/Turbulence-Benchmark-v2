def palindrome_of_length_at_least_n(s):
    s = ''.join((char.lower() for char in s if char.isalpha()))
    n = 87
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes