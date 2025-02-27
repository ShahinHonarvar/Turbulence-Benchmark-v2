def return_n_greatest_chars(chars: str) -> list:
    chars = sorted(list(chars), reverse=True)
    return chars[:26]