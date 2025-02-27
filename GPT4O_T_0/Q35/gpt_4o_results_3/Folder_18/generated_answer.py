def remove_repeat_chars(s):
    if len(s) <= 56:
        return s
    sub_str = s[57:90]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 56 or s.index(char) >= 90))
    return result