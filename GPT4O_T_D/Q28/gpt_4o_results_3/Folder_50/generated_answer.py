def return_nth_smallest_ascii(s):
    filtered_chars = s[25:89]
    sorted_chars = sorted(filtered_chars, key=ord)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]