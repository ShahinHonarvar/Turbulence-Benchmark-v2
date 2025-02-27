def return_nth_smallest_ascii(input_string):
    chars = list(input_string[:9])
    sorted_chars = sorted(chars, key=lambda char: ord(char))
    return sorted_chars[8]