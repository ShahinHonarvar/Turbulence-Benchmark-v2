def remove_repeat_chars(s):
    if len(s) <= 26:
        return s
    end = min(80, len(s))
    substring = s[26:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 26 or i >= 80 or char not in repeated_chars:
            result.append(char)
    return ''.join(result)