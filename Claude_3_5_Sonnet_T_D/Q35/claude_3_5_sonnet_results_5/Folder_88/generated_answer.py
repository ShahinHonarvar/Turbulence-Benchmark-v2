def remove_repeat_chars(s):
    target_substr = s[4:9]
    char_count = {}
    for char in target_substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))