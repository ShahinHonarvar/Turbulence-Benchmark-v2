def remove_repeat_chars(s):
    if len(s) <= 543:
        return s
    segment = s[331:543]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif char in repeat_chars:
            repeat_chars.remove(char)
    return ''.join(result)