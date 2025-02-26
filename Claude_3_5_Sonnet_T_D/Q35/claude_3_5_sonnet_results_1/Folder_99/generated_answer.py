def remove_repeat_chars(string):
    if len(string) <= 451:
        return string
    start = 451
    end = min(905, len(string))
    substring = string[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(string):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)