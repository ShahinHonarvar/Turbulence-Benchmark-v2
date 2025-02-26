def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    start = 44
    end = min(70, len(s))
    substring = s[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)