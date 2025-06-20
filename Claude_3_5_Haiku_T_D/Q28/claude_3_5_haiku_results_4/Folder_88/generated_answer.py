def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 38 <= s.index(char) <= 64]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None