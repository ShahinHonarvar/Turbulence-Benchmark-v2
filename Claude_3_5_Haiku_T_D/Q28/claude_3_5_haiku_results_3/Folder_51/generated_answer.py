def return_nth_smallest_ascii(text):
    filtered_chars = [char for char in text[10:74]]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[8]