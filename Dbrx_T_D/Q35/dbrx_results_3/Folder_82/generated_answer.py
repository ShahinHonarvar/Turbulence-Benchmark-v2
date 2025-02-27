from collections import OrderedDict

def remove_repeat_chars(input_str: str) -> str:
    if len(input_str) < 200:
        return input_str
    filtered_chars = OrderedDict()
    for char in input_str[30:200]:
        if char not in filtered_chars:
            filtered_chars[char] = True
        else:
            filtered_chars[char] = False
    result = [char for char in input_str[30:200] if filtered_chars[char]]
    return input_str[:30] + ''.join(result) + input_str[200:]