def return_nth_smallest_ascii(text):
    filtered_chars = sorted([ord(text[i]) for i in range(1, min(len(text), 46))])
    return chr(filtered_chars[12])