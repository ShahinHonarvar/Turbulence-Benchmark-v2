def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 54
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(n, len(s) - i + 1):
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes