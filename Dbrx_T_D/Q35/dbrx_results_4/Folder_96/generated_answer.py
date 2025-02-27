def remove_repeat_chars(input_str: str) -> str:
    for char in set(input_str[60:200]):
        if input_str[60:200].count(char) > 1:
            input_str = input_str.replace(char, '', input_str[60:200].count(char))
    return input_str