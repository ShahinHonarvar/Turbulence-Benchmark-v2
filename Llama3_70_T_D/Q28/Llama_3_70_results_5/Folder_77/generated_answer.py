def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(63, 77)]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[13]