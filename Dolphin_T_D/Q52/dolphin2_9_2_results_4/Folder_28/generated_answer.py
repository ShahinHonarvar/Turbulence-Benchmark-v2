def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) == 43:
                palindromes.add(sub)
    return palindromes