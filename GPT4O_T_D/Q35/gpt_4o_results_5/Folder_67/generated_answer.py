def remove_repeat_chars(s):
    sub_str = s[45:67]
    char_count = {}
    for char in sub_str:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result