def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    char_count = {}
    for i in range(51, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)