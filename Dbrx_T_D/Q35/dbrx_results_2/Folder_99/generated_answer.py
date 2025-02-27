import string

def remove_repeat_chars(input_string: str) -> str:
    substring = input_string[450:905]
    char_set = set(substring)
    for char in char_set:
        if substring.count(char) > 1:
            input_string = input_string.replace(char, '', substring.count(char))
    return input_string