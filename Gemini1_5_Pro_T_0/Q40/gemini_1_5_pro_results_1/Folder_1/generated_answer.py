def return_n_smallest_chars(string: str) -> list:
    sorted_chars = sorted(string)
    return sorted(sorted_chars[:11], reverse=True)