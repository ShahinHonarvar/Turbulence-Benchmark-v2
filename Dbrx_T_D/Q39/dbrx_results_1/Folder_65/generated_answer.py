def return_n_greatest_chars(input_string: str) -> list:
    input_string = ''.join((c for c in input_string if c.isalpha()))
    return sorted(input_string, key=ord, reverse=True)[:27]