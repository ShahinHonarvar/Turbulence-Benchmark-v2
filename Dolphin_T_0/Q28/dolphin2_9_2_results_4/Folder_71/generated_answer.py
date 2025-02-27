def return_nth_smallest_ascii(s):
    sorted_chars = sorted([s[i] for i in range(5, 83)])
    return sorted_chars[15]