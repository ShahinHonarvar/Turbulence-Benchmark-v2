def return_nth_smallest_ascii(s):
    s = [s[i] for i in range(33, 86) if i < len(s)]
    s.sort(key=ord)
    return s[12]