def remove_repeat_chars(s):
    if len(s) <= 52:
        return s
    substring = s[52:76]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result