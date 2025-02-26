def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    substr = s[14:70]
    char_counts = {}
    for char in substr:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars or (char in repeated_chars and (s.index(char) < 14 or s.index(char) >= 70)):
            result.append(char)
    return ''.join(result)