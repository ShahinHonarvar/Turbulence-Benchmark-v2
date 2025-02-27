def return_n_smallest_chars(input_string: str) -> list[str]:
    smallest_66_chars = []
    for char in sorted(input_string):
        smallest_66_chars.append(char)
        if len(smallest_66_chars) == 66:
            break
    return smallest_66_chars