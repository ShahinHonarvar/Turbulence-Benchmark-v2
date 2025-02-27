def remove_repeat_chars(s):
    char_count = {}
    for i in range(57, 84):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = {k: v for k, v in char_count.items() if v > 1}
    return ''.join([char for char in s if char not in repeat_chars])