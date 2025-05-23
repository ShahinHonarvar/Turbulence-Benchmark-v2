def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    substring = s[44:70]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or s.index(char) < 44 or s.index(char) >= 70:
            result.append(char)
    return ''.join(result)