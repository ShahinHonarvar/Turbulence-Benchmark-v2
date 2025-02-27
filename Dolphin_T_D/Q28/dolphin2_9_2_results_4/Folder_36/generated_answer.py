def return_nth_smallest_ascii(s):
    sorted_ascii = sorted([s[i] for i in range(17, 57)])
    return sorted_ascii[8]