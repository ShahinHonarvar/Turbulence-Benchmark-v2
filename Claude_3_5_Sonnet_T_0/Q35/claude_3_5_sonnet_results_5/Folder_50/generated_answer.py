def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    end = min(76, len(s))
    substring = s[13:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = s[:13] + ''.join((char for char in s[13:end] if char not in chars_to_remove)) + s[end:]
    return result