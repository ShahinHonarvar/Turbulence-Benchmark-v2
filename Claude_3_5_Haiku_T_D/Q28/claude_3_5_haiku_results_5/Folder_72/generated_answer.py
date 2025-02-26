def return_nth_smallest_ascii(chars):
    filtered_chars = [char for char in chars if 33 <= chars.index(char) <= 60]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[17]