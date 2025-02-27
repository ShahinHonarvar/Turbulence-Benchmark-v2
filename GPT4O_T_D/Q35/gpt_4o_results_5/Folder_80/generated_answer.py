def remove_repeat_chars(s):
    target_range = s[58:84]
    char_count = {}
    for char in target_range:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or not 58 < s.index(char) < 84))