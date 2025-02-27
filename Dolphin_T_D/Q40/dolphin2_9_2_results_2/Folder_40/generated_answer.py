def return_n_smallest_chars(s):
    l = []
    for char in s:
        if len(l) < 7:
            l.append(char)
        else:
            break
    return sorted(l, key=lambda x: ord(x), reverse=True)