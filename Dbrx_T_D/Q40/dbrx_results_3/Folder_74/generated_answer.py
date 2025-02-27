def return_n_smallest_chars(string_of_chars: str) -> list[str]:
    sorted_chars = sorted(string_of_chars)
    return sorted_chars[:5]