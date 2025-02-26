def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 33 <= s.index(char) <= 85]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None