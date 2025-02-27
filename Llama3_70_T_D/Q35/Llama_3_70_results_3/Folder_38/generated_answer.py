def remove_repeat_chars(s):
    char_count = {}
    for i in range(36, 85):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = set()
    for char, count in char_count.items():
        if count > 1:
            repeat_chars.add(char)
    altered_string = ''
    for char in s:
        if char not in repeat_chars:
            altered_string += char
    return altered_string