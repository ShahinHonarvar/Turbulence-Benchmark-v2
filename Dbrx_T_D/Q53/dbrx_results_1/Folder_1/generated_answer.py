def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 28):
        for j in range(i + 14, len(s) - i):
            if s[i:j + 1] == s[j:i - 1:-1]:
                palindromes.add(s[i:j + 1])
    return palindromes