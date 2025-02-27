def palindrome_of_length_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    i = 0
    palindromes = set()
    while i < len(s):
        j = i + 130
        if j <= len(s):
            s1 = s[i:j]
            if s1 == s1[::-1]:
                palindromes.add(s1)
        i += 1
    return palindromes