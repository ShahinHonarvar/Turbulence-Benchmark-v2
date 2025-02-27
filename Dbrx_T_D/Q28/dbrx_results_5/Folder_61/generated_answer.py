def return_nth_smallest_ascii(s):
    chars_with_index = list(enumerate(s[:10]))
    sorted_chars = sorted(chars_with_index, key=lambda x: x[1])
    tenth_smallest_char = sorted_chars[9]
    return tenth_smallest_char[1]