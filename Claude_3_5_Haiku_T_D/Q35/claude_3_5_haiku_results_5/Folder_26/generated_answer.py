def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    segment = s[69:99]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or s.index(char) < 69 or s.index(char) >= 99:
            result.append(char)
    return ''.join(result)