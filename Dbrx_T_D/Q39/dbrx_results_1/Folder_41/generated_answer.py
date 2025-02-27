def return_n_greatest_chars(s: str) -> str:
    return ''.join(sorted(s, reverse=True)[:37])