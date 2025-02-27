def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string)
    smallest_24_chars = input_string_sorted[:24]
    smallest_24_chars.reverse()
    return smallest_24_chars