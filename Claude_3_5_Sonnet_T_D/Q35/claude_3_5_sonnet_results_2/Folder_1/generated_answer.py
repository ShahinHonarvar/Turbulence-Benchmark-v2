def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    end = min(88, len(s))
    substring = s[17:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 17 or i >= 88 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)