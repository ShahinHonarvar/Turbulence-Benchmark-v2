def remove_repeat_chars(string):
    if len(string) <= 71:
        return string
    target_section = string[71:98]
    char_count = {}
    for char in target_section:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''
    for char in string:
        if char not in repeat_chars:
            result += char
    return result