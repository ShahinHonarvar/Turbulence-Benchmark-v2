def return_n_greatest_chars(string_of_chars: str) -> list:
    ascii_values_of_chars = sorted(list(map(ord, string_of_chars)), reverse=True)
    n_greatest_ascii_values = ascii_values_of_chars[:76]
    return [chr(ascii) for ascii in n_greatest_ascii_values]