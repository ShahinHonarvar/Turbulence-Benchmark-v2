def return_nth_smallest_ascii(s):
    v = [(s[i], ord(s[i])) for i in range(33, 86)]
    v.sort(key=lambda x: x[1])
    return v[19][0]