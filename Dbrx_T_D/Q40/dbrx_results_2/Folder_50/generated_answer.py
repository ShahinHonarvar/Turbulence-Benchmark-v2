def return_n_smallest_chars(input_string: str) -> list:
    chars = list(map(ord, input_string))
    chars.sort()
    smallest_chars = chars[:16]
    smallest_chars.sort(reverse=True)
    return [chr(ascii_value) for ascii_value in smallest_chars]