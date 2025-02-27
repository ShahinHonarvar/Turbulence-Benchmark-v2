def return_n_smallest_chars(string_of_chars: str) -> list:
    return sorted(list(string_of_chars), key=ord, reverse=True)[:85]