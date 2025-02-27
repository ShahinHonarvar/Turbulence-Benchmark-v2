def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 392, len(s)):
            sub = s[i:j + 392]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes