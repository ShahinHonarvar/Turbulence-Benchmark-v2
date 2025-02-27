def return_n_smallest_chars(string_of_chars: str) -> list:
    sorted_chars = sorted(set(string_of_chars), key=ord)
    return sorted_chars[-47:][::-1]