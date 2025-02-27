def remove_repeat_chars(s):
    if len(s) < 90:
        return s
    sub_str = s[87:90]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))