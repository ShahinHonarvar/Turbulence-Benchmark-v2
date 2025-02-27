def return_nth_smallest_ascii(s):
    ascii_val = []
    for i in range(14, 55):
        if s[i] not in ascii_val:
            ascii_val.append(s[i])
    ascii_val.sort()
    return ascii_val[10]