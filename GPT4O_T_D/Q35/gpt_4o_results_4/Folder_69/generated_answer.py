def remove_repeat_chars(s):
    if len(s) > 43:
        sub_str = s[40:43]
        char_counts = {char: sub_str.count(char) for char in sub_str}
        chars_to_remove = {char for char, count in char_counts.items() if count > 1}
        result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 40 or s.index(char) >= 43))
        return result
    return s