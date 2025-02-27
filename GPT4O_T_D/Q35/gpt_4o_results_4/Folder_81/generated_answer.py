def remove_repeat_chars(s):
    if len(s) <= 20:
        return s
    substr = s[21:200] if len(s) > 200 else s[21:]
    char_count = {}
    for char in substr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for index, char in enumerate(s):
        if not (21 <= index < 200 and char in chars_to_remove):
            result.append(char)
    return ''.join(result)