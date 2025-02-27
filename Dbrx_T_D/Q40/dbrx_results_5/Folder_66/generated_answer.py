def return_n_smallest_chars(string_of_chars: str) -> list[str]:
    chars_list = sorted(list(string_of_chars)) + [''] * (33 - len(chars_list))
    return chars_list[:33][::-1]