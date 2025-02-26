def remove_repeat_chars(s):
    segment = s[11:28]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''
    for i, char in enumerate(s):
        if i < 11 or i >= 28 or char not in repeated_chars:
            result += char
    return result