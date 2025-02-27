def palindrome_of_length_n(s):
    s = s.lower()
    n = 7
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes