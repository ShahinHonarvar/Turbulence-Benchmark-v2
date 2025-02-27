def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 10:
            smallest_chars.append(char)
        else:
            smallest_chars.sort()
            if char < smallest_chars[-1]:
                smallest_chars[-1] = char
    return smallest_chars