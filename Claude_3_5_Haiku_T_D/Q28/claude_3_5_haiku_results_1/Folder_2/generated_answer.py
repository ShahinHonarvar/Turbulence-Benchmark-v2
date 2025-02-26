def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 48 <= s.index(char) <= 76]
    return sorted(filtered_chars)[4] if len(filtered_chars) >= 5 else None