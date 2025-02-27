def return_n_smallest_chars(input_string: str) -> list[str]:
    input_string = ''.join(sorted(input_string))
    return list(input_string[:87])