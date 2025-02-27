def remove_repeat_chars(s):
    seen_chars = set()
    chars_to_remove = set()
    for i in range(45, 90):
        char = s[i]
        if char in seen_chars:
            chars_to_remove.add(char)
        else:
            seen_chars.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)