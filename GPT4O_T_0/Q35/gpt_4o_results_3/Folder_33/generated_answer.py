def remove_repeat_chars(s):
    if len(s) <= 125:
        return s
    start = 126
    end = min(825, len(s) - 1)
    substring = s[start:end]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i <= 125 or i >= 825 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)