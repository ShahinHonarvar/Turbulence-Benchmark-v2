def return_n_greatest_chars(s: str) -> list:
    return sorted(s, key=lambda char: ord(char), reverse=True)[:11]