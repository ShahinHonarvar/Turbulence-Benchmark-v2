def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 23):
        sub = s[i:i + 24]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes