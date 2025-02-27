def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 7):
            if s[i:j] == s[i:j][::-1] and s[i:j]:
                palindromes.add(s[i:j])
    return palindromes