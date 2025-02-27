def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes