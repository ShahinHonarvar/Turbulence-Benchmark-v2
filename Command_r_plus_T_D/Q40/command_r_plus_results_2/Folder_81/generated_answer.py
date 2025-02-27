def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string)
    smallest_64_chars = sorted_string[:64]
    return smallest_64_chars