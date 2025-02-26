def return_nth_smallest_ascii(s):
    filtered_chars = [char for index, char in enumerate(s) if 47 <= index <= 80]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None