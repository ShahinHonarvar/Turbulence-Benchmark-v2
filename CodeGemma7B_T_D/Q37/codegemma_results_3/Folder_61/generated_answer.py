def filter_chars(n):
    s = list(n)
    for i in range(5, 7):
        s = [j for j in s if j != s[i]]
    return ''.join(s)