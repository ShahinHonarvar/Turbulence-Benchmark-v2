def remove_repeat_chars(s):
    s = list(s)
    char_count = {}
    for char in s[306:807]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    remove_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in remove_chars))