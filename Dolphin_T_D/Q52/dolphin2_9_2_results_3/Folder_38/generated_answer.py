def palindrome_of_length_n(s):
    s = s.lower()
    n = 38
    pals = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            pals.add(sub)
    return pals