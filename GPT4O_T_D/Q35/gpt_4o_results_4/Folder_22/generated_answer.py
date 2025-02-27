def remove_repeat_chars(s):
    sub_str = s[51:200]
    counts = {}
    for char in sub_str:
        counts[char] = counts.get(char, 0) + 1
    for char in sub_str:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s