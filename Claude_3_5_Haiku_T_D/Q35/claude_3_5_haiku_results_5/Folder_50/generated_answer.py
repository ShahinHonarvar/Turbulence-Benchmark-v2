def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    substr = s[14:76]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif s.index(char) >= 14 and s.index(char) < 76:
            continue
        else:
            result.append(char)
    return ''.join(result)