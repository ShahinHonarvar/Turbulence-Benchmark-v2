def return_n_greatest_chars(string_of_chars: str) -> list[str]:
    sorted_chars = sorted(string_of_chars, key=lambda char: ord(char), reverse=True)
    return sorted_chars[:59]