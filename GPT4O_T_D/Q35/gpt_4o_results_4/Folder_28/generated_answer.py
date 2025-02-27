def remove_repeat_chars(s):
    if len(s) <= 86:
        return s
    start, end = (87, 99)
    substring = s[start:end]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars or not start < s.index(char) < end - 1))