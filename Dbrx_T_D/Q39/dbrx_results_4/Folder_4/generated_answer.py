def return_n_greatest_chars(input_str: str) -> list:
    if len(input_str) < 90:
        return sorted(list(input_str), key=ord, reverse=True)
    else:
        return sorted(list(input_str)[-90:], key=ord, reverse=True)