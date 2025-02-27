def return_n_smallest_chars(s: str) -> list[str]:
    s_sorted = sorted(s, key=lambda x: ord(x))
    return s_sorted[:89][::-1]