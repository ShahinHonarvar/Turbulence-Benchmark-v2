def remove_repeat_chars(s):
    if len(s) <= 41:
        return s
    substring = s[41:200]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif char in repeat_chars and (s.index(char) < 41 or s.index(char) >= 200):
            result.append(char)
    return ''.join(result)