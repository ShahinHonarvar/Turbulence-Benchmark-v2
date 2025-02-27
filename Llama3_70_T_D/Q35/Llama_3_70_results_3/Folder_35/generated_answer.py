def remove_repeat_chars(s):
    char_count = {}
    for char in s[77:84]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set([char for char, count in char_count.items() if count > 1])
    return ''.join([char for idx, char in enumerate(s) if char not in repeat_chars or (idx < 77 or idx > 84)])