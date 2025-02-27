def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 59):
        for j in range(i + 30, len(s) - i + 1, 2):
            if s[i:j] == s[j - 1:i - 1:-1]:
                palindromes.add(s[i:j])
    return palindromes