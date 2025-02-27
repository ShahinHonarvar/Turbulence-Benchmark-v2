def remove_repeat_chars(s):
    if len(s) < 14 or len(s) < 77:
        return s
    sub_str = s[14:76]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join([char for char in s if not (s.index(char) > 13 and s.index(char) < 76 and (char in to_remove))])