def return_n_smallest_chars(s: str) -> list[str]:
    s = ''.join(sorted(s))
    return list(s[:76])