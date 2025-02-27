def palindrome_of_length_at_least_n(s):
    ret = set()
    length = len(s)
    for i in range(length):
        for j in range(length, -1, -1):
            sub = s[i:j]
            if len(sub) >= 38:
                sub = sub.lower()
                if sub == sub[::-1]:
                    ret.add(sub)
    return ret