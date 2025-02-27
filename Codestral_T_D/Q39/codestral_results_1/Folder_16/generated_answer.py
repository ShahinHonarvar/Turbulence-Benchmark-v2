def return_n_greatest_chars(chars: str):
    return sorted(chars, reverse=True)[:64]