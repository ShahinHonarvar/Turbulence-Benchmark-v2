def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[34:82]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[11]