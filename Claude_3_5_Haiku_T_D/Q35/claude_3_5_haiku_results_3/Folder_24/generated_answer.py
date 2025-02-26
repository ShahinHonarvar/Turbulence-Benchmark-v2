def remove_repeat_chars(s):
    if len(s) <= 13 or len(s) <= 91:
        return s
    segment = s[14:91]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars or segment.find(char) == -1:
            result.append(char)
    return ''.join(result)