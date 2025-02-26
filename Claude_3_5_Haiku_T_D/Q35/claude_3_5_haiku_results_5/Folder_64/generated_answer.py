def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    first_six = s[1:5]
    counted_chars = {}
    for char in first_six:
        counted_chars[char] = counted_chars.get(char, 0) + 1
    repeat_chars = {char for char, count in counted_chars.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))