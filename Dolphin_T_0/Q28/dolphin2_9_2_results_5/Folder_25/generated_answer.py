def return_nth_smallest_ascii(s):
    ascii_arr = sorted([s[i] for i in range(34, 69)])
    if len(ascii_arr) < 6:
        return None
    else:
        return ascii_arr[5]