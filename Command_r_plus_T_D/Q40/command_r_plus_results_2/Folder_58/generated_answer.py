def return_n_smallest_chars(s: str) -> list[str]:
    return sorted(s, key=lambda char: ord(char), reverse=True)[:49]