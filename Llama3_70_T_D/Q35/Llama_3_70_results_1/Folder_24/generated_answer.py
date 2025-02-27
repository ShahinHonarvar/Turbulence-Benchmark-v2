def remove_repeat_chars(s):
    char_count = {}
    for char in s[13:91]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set()
    for char in char_count:
        if char_count[char] > 1:
            repeat_chars.add(char)
    new_s = ''
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s