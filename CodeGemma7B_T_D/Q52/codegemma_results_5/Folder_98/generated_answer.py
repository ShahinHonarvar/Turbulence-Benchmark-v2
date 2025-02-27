def palindrome_of_length_n(s):
    all_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 5):
        for j in range(i + 3, len(s)):
            if s[i] == s[j] and s[i + 1] == s[j - 1] and (s[i + 2] == s[j - 2]):
                if s[i + 3] == s[j - 3] and s[i + 4] == s[j - 4]:
                    all_palindromes.add(s[i:j + 1])
    return all_palindromes