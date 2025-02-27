def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_chars = []
    for char in sorted(input_string, key=lambda x: ord(x)):
        if len(smallest_chars) < 26:
            smallest_chars.append(char)
        else:
            break
    return smallest_chars[::-1]