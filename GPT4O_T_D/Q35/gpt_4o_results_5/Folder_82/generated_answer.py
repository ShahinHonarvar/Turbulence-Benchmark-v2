def remove_repeat_chars(s):
    if len(s) <= 30:
        return s
    sub_string = s[31:200] if len(s) > 200 else s[31:]
    char_count = {char: sub_string.count(char) for char in set(sub_string)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)