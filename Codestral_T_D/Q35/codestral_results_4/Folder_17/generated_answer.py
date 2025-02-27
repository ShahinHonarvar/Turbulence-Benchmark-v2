def remove_repeat_chars(s):
    char_count = {}
    for i in range(73, 84):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    remove_chars = [char for char, count in char_count.items() if count > 1]
    result = ''.join([c for c in s if c not in remove_chars])
    return result