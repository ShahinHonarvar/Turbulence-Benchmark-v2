def return_n_greatest_chars(string_of_chars: str) -> list[str]:
    sorted_list = sorted(list(string_of_chars), key=ord, reverse=True)
    return sorted_list[:39]