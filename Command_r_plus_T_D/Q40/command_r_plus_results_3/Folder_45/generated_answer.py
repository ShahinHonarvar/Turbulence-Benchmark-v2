def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 52:
            smallest_chars.append(char)
        else:
            smallest_ascii_val = ord(smallest_chars[0])
            if ord(char) < smallest_ascii_val:
                smallest_chars[0] = char
    smallest_chars.sort()
    return smallest_chars