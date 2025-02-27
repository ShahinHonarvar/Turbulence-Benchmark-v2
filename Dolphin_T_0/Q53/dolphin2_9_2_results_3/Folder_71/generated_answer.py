def palindrome_of_length_at_least_n(s):
    palindromes = set()
    length = 87
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + length, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) >= length:
                palindromes.add(sub)
    return palindromes