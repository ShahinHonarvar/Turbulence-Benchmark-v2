def return_n_greatest_chars(string_of_chars: str) -> list[str]:
    return sorted(set(string_of_chars), key=ord, reverse=True)[:29]