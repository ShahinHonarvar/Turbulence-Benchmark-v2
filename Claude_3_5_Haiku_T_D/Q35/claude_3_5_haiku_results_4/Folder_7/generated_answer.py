def remove_repeat_chars(s):
    if len(s) <= 375:
        return s
    substring = s[376:926]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
        elif s.index(char) < 376 or s.index(char) >= 926:
            result += char
    return result