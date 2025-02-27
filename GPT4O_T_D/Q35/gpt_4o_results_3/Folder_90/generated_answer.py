def remove_repeat_chars(s):
    start, end = (307, 807)
    substring = s[start:end]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i <= start or i >= end:
            result.append(char)
        elif char not in chars_to_remove:
            result.append(char)
    return ''.join(result)