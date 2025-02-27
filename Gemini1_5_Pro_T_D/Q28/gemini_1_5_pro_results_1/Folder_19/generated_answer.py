def return_nth_smallest_ascii(text):
    filtered_chars = sorted([ord(text[i]) for i in range(min(19, len(text)))])
    return chr(filtered_chars[12])