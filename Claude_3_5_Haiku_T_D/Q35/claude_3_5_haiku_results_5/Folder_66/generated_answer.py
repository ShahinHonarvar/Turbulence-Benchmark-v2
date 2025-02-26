def remove_repeat_chars(s):
    if len(s) <= 12:
        return s
    substring = s[12:76]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
        elif char in repeat_chars:
            repeat_chars.remove(char)
    return result