def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 94 + 1):
        for j in range(94, 0, -1):
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return {p for p in palindromes if len(p) >= 94}