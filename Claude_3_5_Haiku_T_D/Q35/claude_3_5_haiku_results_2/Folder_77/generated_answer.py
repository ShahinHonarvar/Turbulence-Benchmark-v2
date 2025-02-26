def remove_repeat_chars(string):
    if len(string) <= 355:
        return string
    segment = string[356:988]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in string if char not in repeat_chars))
    return result