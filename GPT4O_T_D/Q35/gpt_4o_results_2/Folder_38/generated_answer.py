def remove_repeat_chars(s):
    sub_string = s[37:85]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) <= 36 or s.index(char) >= 85))