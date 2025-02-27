def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 13):
        for j in range(i + 7, len(s) - i + 1, 2):
            if s[i:j] == s[j - 1:i - 1:-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes