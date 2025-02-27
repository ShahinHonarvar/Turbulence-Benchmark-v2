def remove_repeat_chars(s):
    char_set = set()
    result = []
    for char in s[:3]:
        if char not in char_set:
            char_set.add(char)
            result.append(char)
    for char in s[3:]:
        if char not in char_set:
            result.append(char)
            char_set.add(char)
    return ''.join(result)