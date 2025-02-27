def remove_repeat_chars(s):
    char_count = {}
    for i in range(30, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    return ''.join([char for char in s if char not in repeat_chars])