def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 81 + 1):
        for j in range(81, 0, -1):
            substring = s[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes