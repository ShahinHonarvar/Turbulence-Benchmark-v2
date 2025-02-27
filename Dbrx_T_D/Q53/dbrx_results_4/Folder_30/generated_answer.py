def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 15):
        for j in range(i + 16, len(s) + 1):
            if j - i < 16:
                continue
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes