def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string, key=lambda x: ord(x))
    return input_string_sorted[:82][::-1]