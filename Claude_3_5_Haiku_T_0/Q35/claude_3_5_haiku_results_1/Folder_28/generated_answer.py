def remove_repeat_chars(s):
    if len(s) <= 86:
        return s
    segment = s[87:99]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)