def return_nth_smallest_ascii(s):
    filtered = [char for char in s if 32 <= s.index(char) <= 67]
    sorted_chars = sorted(filtered, key=ord)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None