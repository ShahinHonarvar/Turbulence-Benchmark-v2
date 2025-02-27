def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string_sorted = sorted(input_string, reverse=True)
    n_greatest_chars = input_string_sorted[:37]
    return n_greatest_chars