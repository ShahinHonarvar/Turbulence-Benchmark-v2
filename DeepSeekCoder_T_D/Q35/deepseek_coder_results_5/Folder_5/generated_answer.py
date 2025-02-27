def remove_repeat_chars(s):
    sub_s = s[2:8]
    char_count = {}
    for char in sub_s:
        char_count[char] = char_count.get(char, 0) + 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))