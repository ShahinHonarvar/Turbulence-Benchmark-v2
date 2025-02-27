def remove_repeat_chars(s):
    if len(s) <= 21:
        return s
    if len(s) > 51:
        sub_str = s[21:51]
    else:
        sub_str = s[21:]
    counts = {}
    for char in sub_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)