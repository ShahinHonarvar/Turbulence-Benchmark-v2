def palindrome_of_length_n(s):
    n = 186
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.lower() == sub[::-1].lower():
            palindromes.add(sub)
    return palindromes