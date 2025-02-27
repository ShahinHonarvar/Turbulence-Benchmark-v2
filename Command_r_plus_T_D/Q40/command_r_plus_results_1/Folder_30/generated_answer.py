def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 72:
            smallest_chars.append(char)
        else:
            break
    smallest_chars.sort()
    return smallest_chars