def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    substring = s[33:99]
    char_count = {}
    repeat_chars = set()
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] > 1:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars or (char in repeat_chars and (s.index(char) < 33 or s.index(char) >= 99)):
            result.append(char)
    return ''.join(result)