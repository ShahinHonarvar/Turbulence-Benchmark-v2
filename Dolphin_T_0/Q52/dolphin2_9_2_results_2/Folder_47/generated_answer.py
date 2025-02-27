def palindrome_of_length_n(s):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    n = 34
    pals = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            for char in sub:
                if char not in chars:
                    break
            else:
                pals.add(sub)
    return pals