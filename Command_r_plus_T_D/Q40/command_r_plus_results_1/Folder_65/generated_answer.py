def return_n_smallest_chars(input_string: str) -> list[str]:
    all_chars = list(input_string)
    all_chars.sort()
    return all_chars[:27][::-1]