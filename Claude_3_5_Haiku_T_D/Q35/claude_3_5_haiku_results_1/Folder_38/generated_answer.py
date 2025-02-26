def remove_repeat_chars(s):
    if len(s) <= 36:
        return s
    segment = s[37:85]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeats = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeats:
            result.append(char)
        elif s.index(char) < 37 or s.index(char) >= 85:
            result.append(char)
    return ''.join(result)