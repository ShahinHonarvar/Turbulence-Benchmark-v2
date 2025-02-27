def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 205):
        sub = s[i:i + 206]
        sub = sub.lower()
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes