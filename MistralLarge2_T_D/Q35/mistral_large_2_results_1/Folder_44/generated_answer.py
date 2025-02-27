def remove_repeat_chars(s):
    sub_str = s[36:52]
    char_count = {char: sub_str.count(char) for char in sub_str}
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join([char for char in s if char not in to_remove])