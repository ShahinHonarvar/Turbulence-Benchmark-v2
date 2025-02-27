def return_n_greatest_chars(given_string: str) -> list:
    given_string = sorted(given_string, key=lambda x: ord(x), reverse=True)
    return given_string[:44]