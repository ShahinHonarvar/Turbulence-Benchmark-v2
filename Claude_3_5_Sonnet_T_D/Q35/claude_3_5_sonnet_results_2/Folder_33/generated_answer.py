def remove_repeat_chars(s):
    if len(s) <= 126:
        return s
    start = 126
    end = min(825, len(s))
    char_count = {}
    for i in range(start, end):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)