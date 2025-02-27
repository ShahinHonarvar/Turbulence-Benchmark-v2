def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[25:89]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[10] if len(sorted_chars) > 10 else None