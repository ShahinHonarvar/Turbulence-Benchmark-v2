def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 38 <= i <= 82]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[19] if len(sorted_chars) > 19 else None