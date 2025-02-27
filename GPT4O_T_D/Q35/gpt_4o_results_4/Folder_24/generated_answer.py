def remove_repeat_chars(s):
    char_count = {}
    for i in range(14, 91):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = []
    for i, char in enumerate(s):
        if i <= 13 or i >= 91 or char_count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)