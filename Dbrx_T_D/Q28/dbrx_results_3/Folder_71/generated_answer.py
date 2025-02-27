def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 5 <= i <= 82]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[15]