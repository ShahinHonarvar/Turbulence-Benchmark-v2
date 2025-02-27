def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 12:
            smallest_chars.append(char)
        else:
            index = smallest_chars.index(max(smallest_chars))
            if ord(char) < ord(smallest_chars[index]):
                smallest_chars[index] = char
    return sorted(smallest_chars)