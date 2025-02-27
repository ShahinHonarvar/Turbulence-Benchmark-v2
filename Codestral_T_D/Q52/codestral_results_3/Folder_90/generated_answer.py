def palindrome_of_length_n(s):
    palindromes = set()
    n = 318
    for i in range(len(s) - n + 1):
        sub = s[i:i + n].lower()
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes