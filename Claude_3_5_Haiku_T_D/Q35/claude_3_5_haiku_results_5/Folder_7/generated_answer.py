def remove_repeat_chars(s):
    if len(s) <= 926:
        return s
    segment = s[376:926]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or (s.index(char) < 376 or s.index(char) >= 926):
            result.append(char)
    return ''.join(result)