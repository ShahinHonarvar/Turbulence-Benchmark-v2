def return_n_greatest_chars(string):
    ascii_value_to_char = {ord(char): char for char in string}
    sorted_by_ascii_value = sorted(ascii_value_to_char.items(), reverse=True)
    return [char for _, char in sorted_by_ascii_value[:72]]