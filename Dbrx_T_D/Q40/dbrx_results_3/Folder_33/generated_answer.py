def return_n_smallest_chars(string_of_chars: str) -> list[str]:
    return sorted(list(string_of_chars), reverse=True)[:36]