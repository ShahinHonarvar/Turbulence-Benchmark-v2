def palindrome_of_length_n(s):
    length = 416
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub == sub[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes