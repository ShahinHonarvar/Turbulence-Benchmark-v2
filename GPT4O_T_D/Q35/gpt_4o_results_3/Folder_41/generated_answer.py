def remove_repeat_chars(s):
    sub_str = s[4:8]
    count = {char: sub_str.count(char) for char in set(sub_str)}
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((c for c in s if c not in repeated_chars))