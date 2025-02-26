def remove_repeat_chars(s):
    if len(s) <= 71:
        return s
    start = 71
    end = min(200, len(s))
    substr = s[start:end]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)