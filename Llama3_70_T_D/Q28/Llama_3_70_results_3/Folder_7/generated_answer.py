def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(12, 56) if s[i] not in s[:i]]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[16]