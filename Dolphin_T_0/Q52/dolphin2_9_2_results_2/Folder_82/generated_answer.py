def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 27):
        sub = s[i:i + 28]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes