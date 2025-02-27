def return_n_greatest_chars(string_of_chars: str) -> list:
    ascii_sorted_chars = sorted(set(string_of_chars), reverse=True)
    return ascii_sorted_chars[:10]