def return_n_greatest_chars(input_string: str) -> list:
    if len(input_string) >= 20:
        sorted_chars = sorted(input_string, key=lambda x: ord(x))
        return sorted_chars[-20:]
    else:
        sorted_chars = sorted(input_string, key=lambda x: ord(x))
        return sorted_chars