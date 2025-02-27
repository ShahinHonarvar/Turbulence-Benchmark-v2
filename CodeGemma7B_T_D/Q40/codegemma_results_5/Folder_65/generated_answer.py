def return_n_smallest_chars(characters: str) -> list:
    return sorted(characters, key=ord)[:27][::-1]