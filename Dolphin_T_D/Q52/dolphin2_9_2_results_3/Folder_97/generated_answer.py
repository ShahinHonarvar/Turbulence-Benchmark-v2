def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(210):
            sub = s[i:i + j + 1]
            if sub == sub[::-1] and len(sub) == 210:
                palindromes.add(sub)
    return palindromes