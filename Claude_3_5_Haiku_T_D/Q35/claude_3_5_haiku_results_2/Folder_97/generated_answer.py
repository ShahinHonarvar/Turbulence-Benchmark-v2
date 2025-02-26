def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    substring = s[35:69]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''
    for char in s:
        if char not in repeated_chars:
            result += char
        elif s.index(char) < 35 or s.index(char) >= 69:
            result += char
    return result