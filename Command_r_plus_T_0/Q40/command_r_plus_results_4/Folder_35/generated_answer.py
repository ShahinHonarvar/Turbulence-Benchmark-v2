def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 7:
            smallest_chars.append(char)
            smallest_chars.sort()
        else:
            break
    return smallest_chars