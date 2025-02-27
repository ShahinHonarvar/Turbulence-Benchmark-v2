def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string, key=lambda char: ord(char))
    return sorted_string[:13][::-1]