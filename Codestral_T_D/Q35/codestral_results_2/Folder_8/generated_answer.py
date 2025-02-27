def remove_repeat_chars(s):
    char_count = {}
    for i in range(46, 49):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = [char for char in char_count if char_count[char] > 1]
    result = ''.join([char for char in s if char not in repeat_chars])
    return result