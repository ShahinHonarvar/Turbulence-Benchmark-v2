def return_n_greatest_chars(input_string: str) -> list[str]:
    input_set = set(input_string)
    ascii_sorted_set = sorted(input_set, key=ord)
    n_greatest_chars = ascii_sorted_set[-21:]
    return n_greatest_chars