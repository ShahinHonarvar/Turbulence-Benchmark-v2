def remove_repeat_chars(s):
    if len(s) <= 30:
        return s
    start = 30
    end = min(53, len(s))
    substring = s[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result