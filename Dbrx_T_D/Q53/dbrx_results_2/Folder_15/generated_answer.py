def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 2, len(s) - i + 1):
            if len(s[i:j]) >= 4 and s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes