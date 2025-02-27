def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    mid_section = s[14:76]
    char_count = {}
    for char in mid_section:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)