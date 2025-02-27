def return_n_smallest_chars(given_string: str) -> list:
    given_list = list(given_string)
    given_list.sort(key=ord, reverse=False)
    return given_list[:84]