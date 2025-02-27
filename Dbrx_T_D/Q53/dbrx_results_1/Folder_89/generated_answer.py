def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 42):
        for j in range(43):
            if s[i:i + j] == s[i:i + j][::-1] and j >= 43:
                palindromes.add(s[i:i + j])
    return palindromes