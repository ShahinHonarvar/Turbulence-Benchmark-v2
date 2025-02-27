def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_66_chars = []
    for char in input_string:
        if len(smallest_66_chars) < 66:
            smallest_66_chars.append(char)
        else:
            index = smallest_66_chars.index(max(smallest_66_chars))
            if ord(char) < ord(smallest_66_chars[index]):
                smallest_66_chars[index] = char
    return sorted(smallest_66_chars)