def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    segment = s[18:88]
    char_count = {}
    for char in segment:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or s.index(char) <= 18 or s.index(char) >= 88:
            result.append(char)
    return ''.join(result)