def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 25
    res = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            res.add(substring)
    return res