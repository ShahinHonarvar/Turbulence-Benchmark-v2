def palindrome_of_length_at_least_n(s):
    s = s.lower()
    l = len(s)
    a = {}
    p = set()
    for i in range(l):
        for j in range(i + 2, l + 1):
            a[s[i:j]] = j - i
    for item in a.items():
        if item[1] >= 33:
            if item[0] == item[0][::-1]:
                p.add(item[0])
    return p