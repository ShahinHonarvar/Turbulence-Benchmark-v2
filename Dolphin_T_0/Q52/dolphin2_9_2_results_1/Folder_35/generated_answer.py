def palindrome_of_length_n(s):
    s = s.lower()
    n = 116
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes