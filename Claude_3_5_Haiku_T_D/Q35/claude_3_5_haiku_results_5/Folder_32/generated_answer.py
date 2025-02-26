def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    segment = s[87:90]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars))
    return result