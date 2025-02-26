def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    end = min(70, len(s))
    substring = s[13:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 13 or i >= 70 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)