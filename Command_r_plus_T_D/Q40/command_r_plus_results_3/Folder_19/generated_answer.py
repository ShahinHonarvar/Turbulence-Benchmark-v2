def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 58:
            smallest_chars.append(char)
        else:
            smallest_ascii_val = min(smallest_chars)
            if ord(char) < ord(smallest_ascii_val):
                smallest_chars.remove(smallest_ascii_val)
                smallest_chars.append(char)
    smallest_chars.sort()
    return smallest_chars