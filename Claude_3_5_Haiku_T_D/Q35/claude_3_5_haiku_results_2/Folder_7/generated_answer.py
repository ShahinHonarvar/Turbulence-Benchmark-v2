def remove_repeat_chars(s):
    if len(s) <= 926:
        return s
    substring = s[376:926]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
        elif s.index(char) < 376 or s.index(char) >= 926:
            result.append(char)
    return ''.join(result)