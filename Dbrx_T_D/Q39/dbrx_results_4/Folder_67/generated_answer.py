def return_n_greatest_chars(string_of_chars: str) -> list[str]:
    n = 66
    sorted_chars = sorted(set(string_of_chars), reverse=True)
    return sorted_chars[:n]