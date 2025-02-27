def return_n_greatest_chars(s: str):
    return sorted(sorted(s, reverse=True)[:32])