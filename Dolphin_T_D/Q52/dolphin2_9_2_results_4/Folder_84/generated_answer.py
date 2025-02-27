def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 130):
        sub = s[i:i + 131]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes