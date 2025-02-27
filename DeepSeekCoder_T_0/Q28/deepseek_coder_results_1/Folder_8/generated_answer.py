def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 60 <= i <= 88]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[6] if len(sorted_chars) > 6 else None