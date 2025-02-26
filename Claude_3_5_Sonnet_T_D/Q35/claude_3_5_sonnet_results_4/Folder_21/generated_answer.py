def remove_repeat_chars(s):
    if len(s) <= 463:
        return s
    end = min(995, len(s))
    substring = s[463:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(s):
        if i < 463 or i >= 995 or char not in repeated_chars:
            result.append(char)
    return ''.join(result)