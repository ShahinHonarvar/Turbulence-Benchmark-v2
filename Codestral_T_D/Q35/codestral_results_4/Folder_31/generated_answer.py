def remove_repeat_chars(string):
    chars = string[33:78]
    duplicates = set([x for x in chars if chars.count(x) > 1])
    return ''.join((char for char in string if char not in duplicates))