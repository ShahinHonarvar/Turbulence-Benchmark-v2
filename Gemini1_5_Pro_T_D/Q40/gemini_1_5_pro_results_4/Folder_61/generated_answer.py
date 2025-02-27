def return_n_smallest_chars(s: str) -> list:
    return sorted([c for c in s if ord(c) <= 122], reverse=True)[:66]