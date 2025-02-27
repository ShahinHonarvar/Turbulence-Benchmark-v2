def palindrome_of_length_n(s):
    s = s.lower()
    palindroms = set()
    for i in range(len(s) - 50):
        sub = s[i:i + 51]
        if sub == sub[::-1]:
            palindroms.add(sub)
    return palindroms