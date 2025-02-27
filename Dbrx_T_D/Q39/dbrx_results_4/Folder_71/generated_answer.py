def return_n_greatest_chars(string_of_chars: str) -> list[str]:
    sorted_chars = sorted(set(string_of_chars))
    n_greatest_chars = sorted_chars[::-1][:14][::-1]
    return n_greatest_chars