def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 8 <= s.index(char) <= 65]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None