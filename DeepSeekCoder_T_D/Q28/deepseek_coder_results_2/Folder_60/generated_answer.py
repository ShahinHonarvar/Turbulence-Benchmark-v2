def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 36 <= i <= 79]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[11] if len(sorted_chars) > 11 else None