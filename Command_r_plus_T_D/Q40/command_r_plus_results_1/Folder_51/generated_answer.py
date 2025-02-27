def return_n_smallest_chars(s: str) -> list[str]:
    sorted_s = sorted(s, key=lambda x: ord(x))
    return sorted_s[:45][::-1]