def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 4):
        for j in range(i + 3, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes