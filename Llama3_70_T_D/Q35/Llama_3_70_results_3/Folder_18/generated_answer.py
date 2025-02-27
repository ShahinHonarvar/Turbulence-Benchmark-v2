def remove_repeat_chars(s):
    char_count = {}
    for char in s[56:90]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set()
    for char, count in char_count.items():
        if count > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])