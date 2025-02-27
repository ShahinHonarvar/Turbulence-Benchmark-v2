def remove_repeat_chars(my_string):
    seen_chars = set()
    result = ''
    for index, char in enumerate(my_string):
        if 46 <= index <= 91 and char in seen_chars:
            continue
        seen_chars.add(char)
        result += char
    return result