def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    n = 94
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes