def remove_repeat_chars(string):
    if len(string) <= 11:
        return string
    substring = string[11:28]
    chars_to_remove = set()
    for i in range(len(substring)):
        if substring.count(substring[i]) > 1 and substring[i] not in chars_to_remove:
            chars_to_remove.add(substring[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result