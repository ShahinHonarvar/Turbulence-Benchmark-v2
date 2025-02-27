def remove_repeat_chars(s):
    if len(s) <= 20:
        return s
    sub_str = s[21:200]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i <= 20 or i >= 200 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)