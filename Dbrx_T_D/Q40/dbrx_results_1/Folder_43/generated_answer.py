def return_n_smallest_chars(string: str) -> list:
    characters = sorted(list(string))[::-1]
    return characters[:56]