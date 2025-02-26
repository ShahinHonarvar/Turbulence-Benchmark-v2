def remove_repeat_chars(s):
    if len(s) <= 709:
        return s
    segment = s[477:709]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
        elif s.index(char) < 477 or s.index(char) >= 709:
            result.append(char)
    return ''.join(result)