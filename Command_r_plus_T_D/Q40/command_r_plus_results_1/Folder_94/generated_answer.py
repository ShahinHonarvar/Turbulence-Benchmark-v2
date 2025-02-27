def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string, key=lambda char: ord(char))
    return input_string_sorted[:87][::-1]