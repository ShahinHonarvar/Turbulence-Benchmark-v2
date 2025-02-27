def return_nth_smallest_ascii(text):
    filtered_chars = sorted((ord(c) for i, c in enumerate(text) if 5 <= i <= 82))
    return chr(filtered_chars[15])