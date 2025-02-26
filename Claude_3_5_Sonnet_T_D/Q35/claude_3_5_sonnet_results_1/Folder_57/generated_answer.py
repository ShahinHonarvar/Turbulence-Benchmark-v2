def remove_repeat_chars(s):
    if len(s) <= 26:
        return s
    start = min(25, len(s) - 1)
    end = min(80, len(s))
    substr = s[start:end]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in repeated_chars:
            result.append(char)
    return ''.join(result)