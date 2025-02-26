def remove_repeat_chars(s):
    if len(s) <= 34:
        return s
    segment = s[35:69]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or s.index(char) < 35 or s.index(char) >= 69:
            result.append(char)
    return ''.join(result)