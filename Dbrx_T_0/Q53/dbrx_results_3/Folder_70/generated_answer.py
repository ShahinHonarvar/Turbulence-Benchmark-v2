def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 10):
        for j in range(i + 5, len(s) - i + 1, 2):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= 11:
                palindromes.add(s[i:j])
    return palindromes