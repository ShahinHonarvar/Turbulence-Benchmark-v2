def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(29, 34)]
    sorted_chars = sorted(chars)
    return sorted_chars[4]