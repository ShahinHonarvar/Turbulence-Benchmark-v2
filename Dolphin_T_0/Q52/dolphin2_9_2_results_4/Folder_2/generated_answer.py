def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) == 147:
                if s[i:j] == s[i:j][::-1]:
                    palindromes.add(s[i:j])
    return palindromes