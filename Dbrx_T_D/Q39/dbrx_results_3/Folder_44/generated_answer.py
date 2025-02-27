def return_n_greatest_chars(s: str) -> str:
    return ''.join(sorted(list(set(s)), key=ord, reverse=True)[:73])