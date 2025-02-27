def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 12):
        for j in range(i, min(i + 13, len(s))):
            if s[j] < 'a' or s[j] > 'z':
                break
            pal = s[i:j + 1]
            if pal == pal[::-1] and j - i >= 13:
                palindromes.add(pal)
    return palindromes