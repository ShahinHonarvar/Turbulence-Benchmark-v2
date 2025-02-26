def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(100, len(s))
    middle_section = s[start:end]
    char_count = {}
    for char in middle_section:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)