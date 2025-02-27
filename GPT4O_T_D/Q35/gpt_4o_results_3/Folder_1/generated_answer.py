def remove_repeat_chars(s):
    substring = s[17:88]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    result = []
    for i, char in enumerate(s):
        if i <= 17 or i >= 88:
            result.append(char)
        elif char_count[char] == 1:
            result.append(char)
    return ''.join(result)