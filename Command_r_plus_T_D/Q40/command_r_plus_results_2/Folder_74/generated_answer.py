def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 5:
            smallest_chars.append(char)
            smallest_chars.sort()
        elif char < smallest_chars[-1]:
            smallest_chars.pop()
            smallest_chars.append(char)
            smallest_chars.sort()
    return smallest_chars