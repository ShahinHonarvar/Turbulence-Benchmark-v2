def remove_repeat_chars(s):
    if len(s) <= 28:
        return s
    chars = s[28:96]
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((c for c in s if c not in to_remove or s.index(c) <= 27 or s.index(c) >= 96))
    return result