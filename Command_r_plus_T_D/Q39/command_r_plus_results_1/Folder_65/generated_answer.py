def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string = input_string.strip()
    if not input_string:
        raise ValueError("Input string can't be empty.")
    char_list = list(input_string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:27]