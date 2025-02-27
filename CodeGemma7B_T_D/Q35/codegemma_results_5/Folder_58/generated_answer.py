def remove_repeat_chars(str):
    if len(str) <= 103 or len(str) >= 802:
        return str
    for char in str[103:802]:
        while str.count(char) > 1:
            str = str.replace(char, '', 1)
    return str