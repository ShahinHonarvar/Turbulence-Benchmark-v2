def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(100, len(s))
    substring = s[start:end]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)