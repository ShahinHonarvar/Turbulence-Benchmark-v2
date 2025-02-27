def return_n_smallest_chars(s: str) -> str:
    return ''.join(sorted(s, key=ord)[:43])