def remove_repeat_chars(string):
    if len(string) <= 14:
        return string
    start = 14
    end = min(70, len(string))
    substring = string[start:end]
    char_count = {char: substring.count(char) for char in substring}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(string):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)