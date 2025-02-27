def remove_repeat_chars(s):
    chars_to_remove = set()
    sub_str = s[7:9]
    for char in sub_str:
        if sub_str.count(char) > 1:
            chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result