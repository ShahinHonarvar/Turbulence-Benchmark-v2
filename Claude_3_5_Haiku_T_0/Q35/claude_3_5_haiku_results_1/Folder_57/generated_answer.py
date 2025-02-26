def remove_repeat_chars(s):
    if len(s) <= 26:
        return s
    substring = s[26:80]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or s.index(char) < 26 or s.index(char) >= 80:
            result.append(char)
    return ''.join(result)