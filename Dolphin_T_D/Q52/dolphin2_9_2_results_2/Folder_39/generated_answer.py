def palindrome_of_length_n(s):
    s = s.lower()
    n = 59
    pals = set()
    for i in range(len(s) - n + 1):
        subZ = s[i:i + n]
        sub = ''.join(filter(str.isalpha, subZ))
        if len(sub) == n and sub == sub[::-1]:
            pals.add(sub)
    return pals