def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 68, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) == 68:
                palindromes.add(s[i:j])
    return palindromes