def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string if 8 <= string.index(char) <= 65]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None