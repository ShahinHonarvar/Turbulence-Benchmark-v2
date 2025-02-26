def remove_repeat_chars(s):
    if len(s) <= 104:
        return s
    start = 103
    end = min(802, len(s))
    char_count = {}
    for char in s[start:end]:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char not in chars_to_remove:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)