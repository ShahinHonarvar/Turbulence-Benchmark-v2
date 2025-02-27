def remove_repeat_chars(s):
    char_count = {}
    for i in range(103, 802):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result