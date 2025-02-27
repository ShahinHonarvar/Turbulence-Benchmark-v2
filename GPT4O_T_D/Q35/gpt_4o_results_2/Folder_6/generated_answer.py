def remove_repeat_chars(s):
    if len(s) <= 20:
        return s
    char_count = {}
    for char in s[21:93]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if char in char_count and char_count[char] > 1:
            continue
        result.append(char)
    return ''.join(result)