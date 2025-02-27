def remove_repeat_chars(s):
    sub_str = s[451:905]
    char_counts = {char: sub_str.count(char) for char in sub_str}
    to_remove = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 450 or s.index(char) >= 905))
    return result