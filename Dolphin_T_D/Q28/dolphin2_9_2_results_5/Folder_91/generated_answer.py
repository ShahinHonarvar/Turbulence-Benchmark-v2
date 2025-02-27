def return_nth_smallest_ascii(s):
    sorted_chars = sorted([ch for ch in s[:8]])
    return sorted_chars[7]