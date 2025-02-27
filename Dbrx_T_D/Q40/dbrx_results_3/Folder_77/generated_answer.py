def return_n_smallest_chars(s: str) -> list:
    ascii_list = [ord(c) for c in s]
    ascii_list.sort()
    return [chr(c) for c in ascii_list[:47]]