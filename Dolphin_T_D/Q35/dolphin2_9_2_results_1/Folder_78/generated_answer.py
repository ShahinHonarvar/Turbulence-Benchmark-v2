def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if 62 <= ord(char) <= 96:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s