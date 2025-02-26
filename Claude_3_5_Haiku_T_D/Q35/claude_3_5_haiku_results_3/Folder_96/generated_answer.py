def remove_repeat_chars(s):
    if len(s) <= 260:
        return s
    segment = s[61:200]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeats = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeats or (s.index(char) < 61 or s.index(char) >= 200):
            result.append(char)
    return ''.join(result)