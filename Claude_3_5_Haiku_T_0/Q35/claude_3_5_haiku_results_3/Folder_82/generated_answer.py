def remove_repeat_chars(s):
    if len(s) <= 31:
        return s
    substring = s[31:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or s.index(char) < 31 or s.index(char) >= 200:
            result.append(char)
    return ''.join(result)