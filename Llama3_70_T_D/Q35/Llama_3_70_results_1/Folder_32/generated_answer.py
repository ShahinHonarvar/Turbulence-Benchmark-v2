def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in s[86:90]:
        if s[86:90].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join([char for i, char in enumerate(s) if (i < 86 or i >= 90) or char not in chars_to_remove])