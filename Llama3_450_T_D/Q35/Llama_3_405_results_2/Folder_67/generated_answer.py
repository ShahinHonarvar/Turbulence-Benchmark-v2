def remove_repeat_chars(s):
    mid_string = s[44:67]
    char_count = {}
    for char in mid_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set([char for char, count in char_count.items() if count > 1])
    return ''.join([char for char in s if char not in repeat_chars])