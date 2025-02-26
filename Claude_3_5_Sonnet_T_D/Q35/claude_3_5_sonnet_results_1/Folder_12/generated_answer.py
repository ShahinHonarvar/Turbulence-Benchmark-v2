def remove_repeat_chars(s):
    if len(s) <= 17:
        return s
    end = min(87, len(s))
    substring = s[16:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < 16 or i >= 87 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)