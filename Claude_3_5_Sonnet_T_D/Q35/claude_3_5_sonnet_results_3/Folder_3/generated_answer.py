def remove_repeat_chars(s):
    if len(s) <= 57:
        return s
    start = 57
    end = min(88, len(s))
    section = s[start:end]
    char_count = {}
    for char in section:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for i, char in enumerate(s):
        if i < start or i >= end or char not in repeated_chars:
            result += char
    return result