def remove_repeat_chars(s):
    if len(s) <= 308:
        return s
    substr = s[307:807]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)