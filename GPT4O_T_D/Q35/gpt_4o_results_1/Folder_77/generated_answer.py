def remove_repeat_chars(input_string):
    sub_string = input_string[356:988]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in input_string if char not in repeated_chars or input_string.index(char) <= 355 or input_string.index(char) >= 988]
    return ''.join(result)