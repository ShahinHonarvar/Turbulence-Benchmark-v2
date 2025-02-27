def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    substring = s[14:70]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or s.index(char) <= 13 or s.index(char) >= 70:
            result.append(char)
    return ''.join(result)