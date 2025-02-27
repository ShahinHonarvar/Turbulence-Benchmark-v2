def remove_repeat_chars(s):
    section = s[37:52]
    char_count = {}
    for char in section:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 36 < s.index(char) < 52))
    return result