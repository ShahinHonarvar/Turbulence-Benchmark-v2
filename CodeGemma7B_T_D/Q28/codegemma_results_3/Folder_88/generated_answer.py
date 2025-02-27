def return_nth_smallest_ascii(str):
    for char in str[38:65]:
        if ord(char) < min_ascii:
            min_ascii = ord(char)
            result = char
    return min_ascii