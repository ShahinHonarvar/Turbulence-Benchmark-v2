def remove_repeat_chars(s):
    if len(s) <= 17:
        return s
    start = 16
    end = min(87, len(s))
    char_count = {}
    for char in s[start:end]:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in repeated_chars:
            result.append(char)
    return ''.join(result)