def remove_repeat_chars(s):
    if len(s) <= 28:
        return s
    sub_str = s[28:96]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for idx, char in enumerate(s):
        if idx <= 27 or idx >= 96 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)