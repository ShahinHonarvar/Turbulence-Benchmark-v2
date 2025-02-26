def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    segment = s[14:76]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or (s.index(char) >= 14 and s.index(char) < 76):
            result.append(char)
    return ''.join(result)