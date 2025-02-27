def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(10, 74)]
    sorted_chars = sorted(chars)
    return sorted_chars[8]