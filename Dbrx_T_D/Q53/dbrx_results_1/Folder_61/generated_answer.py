def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha() and (len(s[i:j + 1]) >= 5):
                palindromes.add(s[i:j + 1])
    return palindromes