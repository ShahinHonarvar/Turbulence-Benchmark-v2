def remove_repeat_chars(s):
    if len(s) <= 104:
        return s
    sub_str = s[104:802]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i <= 103 or i >= 802 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)