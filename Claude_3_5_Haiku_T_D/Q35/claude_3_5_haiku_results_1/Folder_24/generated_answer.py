def remove_repeat_chars(s):
    if len(s) <= 13 or len(s) <= 91:
        return s
    substring = s[14:91]
    char_count = {}
    repeat_chars = set()
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] > 1:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif char in repeat_chars and (s.index(char) < 14 or s.index(char) >= 91):
            result.append(char)
    return ''.join(result)