def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 5):
        sub = s[i:i + 6]
        if sub == sub[::-1] and 'a' <= sub[0] <= 'z':
            palindromes.add(sub)
    return palindromes