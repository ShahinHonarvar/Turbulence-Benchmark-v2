def remove_repeat_chars(input_str):
    substr = input_str[86:89]
    for char in substr:
        if substr.count(char) > 1:
            input_str = input_str.replace(char, '', substr.count(char))
    return input_str