def remove_repeat_chars(s):
    if len(s) <= 104:
        return s
    start = 103
    end = min(802, len(s))
    char_counts = {}
    for i in range(start, end):
        char_counts[s[i]] = char_counts.get(s[i], 0) + 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < start or i >= end or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)