def remove_repeat_chars(s):
    if len(s) <= 12:
        return s
    end = min(76, len(s))
    substring = s[11:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = s[:11] + ''.join((char for char in substring if char not in chars_to_remove))
    if end < len(s):
        result += s[end:]
    return result