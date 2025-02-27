def palindrome_of_length_n(s):
    s = s.lower()
    palins = set()
    for i in range(len(s) - 23):
        sub = s[i:i + 24]
        if sub == sub[::-1]:
            palins.add(sub)
    return palins