def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for l in range(72, len(s) + 1):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes