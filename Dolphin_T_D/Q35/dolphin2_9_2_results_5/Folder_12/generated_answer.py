def remove_repeat_chars(s):
    char_count = {}
    for char in s[16:87]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s[:16]:
        if char in char_count and char_count[char] > 0:
            s = s.replace(char, '')
    for char in s[87:]:
        if char in char_count and char_count[char] > 0:
            s = s.replace(char, '')
    return s