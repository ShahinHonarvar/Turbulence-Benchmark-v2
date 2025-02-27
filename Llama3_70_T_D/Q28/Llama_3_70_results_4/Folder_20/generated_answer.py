def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(25, 65)]
    sixth_smallest_ascii = sorted(chars_in_range)[5]
    return sixth_smallest_ascii