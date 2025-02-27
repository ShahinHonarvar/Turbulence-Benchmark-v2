def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    char_count = {}
    for char in s[35:69]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 34 or s.index(char) >= 69))