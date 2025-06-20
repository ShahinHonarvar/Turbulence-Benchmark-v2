def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 80 + 1):
        for j in range(i + 40, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1] not in palindromes:
                palindromes.add(s[i:j + 1])
    return palindromes