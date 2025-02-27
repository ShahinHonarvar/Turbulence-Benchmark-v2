def palindrome_of_length_n(s):
    s = s.lower()
    n = 181
    palindromes = set()
    palindrome = ''
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes