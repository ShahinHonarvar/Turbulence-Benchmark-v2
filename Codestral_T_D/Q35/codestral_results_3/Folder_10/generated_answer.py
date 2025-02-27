def remove_repeat_chars(s):
    substring = s[36:54]
    repeat_chars = set()
    for char in substring:
        if substring.count(char) > 1:
            repeat_chars.add(char)
    altered_string = ''
    for char in s:
        if char not in repeat_chars:
            altered_string += char
    return altered_string