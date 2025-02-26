def remove_repeat_chars(s):
    if len(s) <= 58:
        return s
    start = 58
    end = min(85, len(s))
    section = s[start:end]
    char_count = {}
    for char in section:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)