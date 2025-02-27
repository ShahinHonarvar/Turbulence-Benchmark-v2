def palindrome_of_length_n(s):
    palindromes = set()
    length = 10
    s = s.lower()
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes