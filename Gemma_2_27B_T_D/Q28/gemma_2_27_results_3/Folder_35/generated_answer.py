def return_nth_smallest_ascii(text):
    substring = text[50:76]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[6]