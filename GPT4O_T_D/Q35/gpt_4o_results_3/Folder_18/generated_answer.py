def remove_repeat_chars(s):
    sub_str = s[57:90]
    repeat_chars = set()
    seen_chars = set()
    for char in sub_str:
        if char in seen_chars:
            repeat_chars.add(char)
        else:
            seen_chars.add(char)
    result = ''.join([char for char in s if char not in repeat_chars])
    return result