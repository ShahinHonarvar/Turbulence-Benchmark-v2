def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    start = 43
    end = min(87, len(s))
    substring = s[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in repeat_chars:
            result.append(char)
    return ''.join(result)