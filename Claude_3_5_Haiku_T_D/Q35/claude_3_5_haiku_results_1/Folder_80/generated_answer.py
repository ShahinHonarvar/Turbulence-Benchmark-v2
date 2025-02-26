def remove_repeat_chars(s):
    if len(s) <= 57:
        return s
    substring = s[58:84]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    result = []
    for char in s:
        if char not in repeat_chars or (s.index(char) < 58 or s.index(char) >= 84):
            result.append(char)
    return ''.join(result)