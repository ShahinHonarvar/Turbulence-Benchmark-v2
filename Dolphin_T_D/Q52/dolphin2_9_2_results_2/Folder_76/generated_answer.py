def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 257, n):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes