def remove_repeat_chars(s):
    if len(s) <= 56:
        return s
    substring = s[57:88]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
        elif s.index(char) < 57 or s.index(char) >= 88:
            result.append(char)
    return ''.join(result)