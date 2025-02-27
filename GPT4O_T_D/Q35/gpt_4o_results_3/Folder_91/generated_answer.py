def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    substring = s[1:6]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    result = []
    for char in s:
        if s.index(char) > 0 and s.index(char) < 6 and (char_count.get(char, 0) > 1):
            continue
        result.append(char)
    return ''.join(result)