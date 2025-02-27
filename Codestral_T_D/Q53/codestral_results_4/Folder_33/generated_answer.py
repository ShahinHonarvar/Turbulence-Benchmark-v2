def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 141
    l = len(s)
    s = s.lower()
    for i in range(l):
        for j in range(i + n, l + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes