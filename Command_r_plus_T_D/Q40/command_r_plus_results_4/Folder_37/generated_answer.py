def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in input_string:
        if len(smallest_chars) < 26:
            smallest_chars.append(char)
        else:
            smallest_chars.sort()
            if char < smallest_chars[-1]:
                smallest_chars[-1] = char
    smallest_chars.sort(reverse=True)
    return smallest_chars