def return_nth_smallest_ascii(s):
    s = s[20:81]
    chars_set = set(s)
    chars_sorted_by_ascii = sorted(chars_set)
    return chars_sorted_by_ascii[10]