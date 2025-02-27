def remove_repeat_chars(s):
    if len(s) <= 376:
        return s
    repeat_section = s[376:926]
    char_count = {}
    for char in repeat_section:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if not (376 < i < 926 and char in chars_to_remove):
            result.append(char)
    return ''.join(result)