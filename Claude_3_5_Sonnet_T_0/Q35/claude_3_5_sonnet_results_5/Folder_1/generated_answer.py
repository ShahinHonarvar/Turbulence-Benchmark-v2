def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    end = min(88, len(s))
    substring = s[17:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = s[:17] + ''.join((char for char in s[17:end] if char not in chars_to_remove)) + s[end:]
    return result