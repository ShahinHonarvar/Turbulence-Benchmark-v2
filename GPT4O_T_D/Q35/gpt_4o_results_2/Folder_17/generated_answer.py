def remove_repeat_chars(s):
    if len(s) <= 74:
        return s
    sub_str = s[74:84]
    counts = {}
    for char in sub_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))