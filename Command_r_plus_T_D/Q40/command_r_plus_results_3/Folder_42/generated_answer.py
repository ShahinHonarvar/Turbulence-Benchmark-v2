def return_n_smallest_chars(input_string: str) -> list[str]:
    return sorted(input_string, key=lambda x: ord(x))[:59][::-1]