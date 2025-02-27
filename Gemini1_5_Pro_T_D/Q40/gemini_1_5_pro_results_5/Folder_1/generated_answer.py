def return_n_smallest_chars(string: str) -> list:
    sorted_string = sorted(string)
    return sorted(sorted_string[:11], reverse=True)