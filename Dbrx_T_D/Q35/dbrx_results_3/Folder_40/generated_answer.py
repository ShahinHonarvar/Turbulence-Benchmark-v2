def remove_repeat_chars(string):
    used_chars = set()
    result = ''
    for char in string[1:4]:
        if char not in used_chars:
            result += char
            used_chars.add(char)
    return string[0] + result + string[4:]