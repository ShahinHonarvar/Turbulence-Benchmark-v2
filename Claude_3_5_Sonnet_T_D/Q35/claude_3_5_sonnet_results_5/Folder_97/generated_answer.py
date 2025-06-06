def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    start = 35
    end = min(69, len(s))
    target_substring = s[start:end]
    char_count = {}
    for char in target_substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in repeated_chars:
            result.append(char)
    return ''.join(result)