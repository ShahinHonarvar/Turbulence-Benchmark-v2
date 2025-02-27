def palindrome_of_length_n(s):
    s = s.lower()
    n = 16
    palindromes = set()
    for i in range(len(s)):
        if i + n <= len(s):
            sub = s[i:i + n]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes