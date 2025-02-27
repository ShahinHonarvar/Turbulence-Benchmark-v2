def return_n_greatest_chars(chars: str) -> list:
    chars = list(chars)
    chars.sort(key=ord, reverse=True)
    return chars[:36]