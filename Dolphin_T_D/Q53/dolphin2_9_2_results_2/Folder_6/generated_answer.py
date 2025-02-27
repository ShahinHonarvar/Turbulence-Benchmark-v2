def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            if len(s[i:j]) >= 22:
                if s[i:j] == ''.join(reversed(s[i:j])):
                    palindromes.add(s[i:j])
    return palindromes