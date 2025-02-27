def remove_repeat_chars(s):
    start, end = (463, 995)
    sub_str = s[start + 1:end]
    char_count = {}
    for char in sub_str:
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