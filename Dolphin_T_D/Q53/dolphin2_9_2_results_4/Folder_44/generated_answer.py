def palindrome_of_length_at_least_n(s):
    a = set()
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            tmp = ''
            for k in range(i, j):
                tmp += s[k].lower()
            if tmp == tmp[::-1] and len(tmp) >= 89:
                a.add(tmp)
    return a