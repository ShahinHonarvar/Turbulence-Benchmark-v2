def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[51:90] if 51 <= s.index(char) <= 89]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[13] if len(sorted_chars) > 13 else None