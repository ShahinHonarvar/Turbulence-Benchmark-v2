def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string)
    smallest_84_chars = sorted_string[:84]
    return smallest_84_chars