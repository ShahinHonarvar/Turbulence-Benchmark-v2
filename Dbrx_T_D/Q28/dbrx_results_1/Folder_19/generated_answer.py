def return_nth_smallest_ascii(s):
    sorted_ascii = sorted(list(set(s[0:19])))
    return chr(sorted_ascii[12])