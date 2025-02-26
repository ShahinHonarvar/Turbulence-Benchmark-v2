def remove_repeat_chars(s):
    if len(s) <= 27:
        return s
    substring = s[28:96]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or (char in repeat_chars and s.index(char) >= 28 and (s.index(char) < 96)):
            result.append(char)
    return ''.join(result)