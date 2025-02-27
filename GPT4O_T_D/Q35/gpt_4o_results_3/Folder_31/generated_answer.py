def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    target_substring = s[34:78]
    char_count = {}
    for char in target_substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 33 or s.index(char) >= 78))
    return result