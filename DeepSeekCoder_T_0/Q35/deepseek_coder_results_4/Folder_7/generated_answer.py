def remove_repeat_chars(s):
    start, end = (376, 926)
    sub_s = s[start:end]
    repeat_chars = {char for char, count in Counter(sub_s).items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)