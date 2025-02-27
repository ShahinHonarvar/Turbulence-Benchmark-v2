def return_n_greatest_chars(string_of_chars: str) -> list:
    return sorted([char for char in set(string_of_chars)], key=ord, reverse=True)[:63]