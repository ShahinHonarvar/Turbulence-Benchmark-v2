def return_n_smallest_chars(ascii_string: str) -> list:
    chars_list = [char for char in ascii_string]
    chars_list.sort(key=lambda char: ord(char))
    return chars_list[:43][::-1]