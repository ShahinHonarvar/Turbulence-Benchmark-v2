def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    substring = s[14:70]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''
    for char in s:
        if char not in repeated_chars or s.index(char) < 14 or s.index(char) >= 70:
            result += char
    return result