def return_n_smallest_chars(input_string: str) -> list[str]:
    sorted_string = sorted(input_string, key=lambda x: ord(x))
    return sorted_string[:11][::-1]