def remove_repeat_chars(s):
    if len(s) <= 12:
        return s
    segment = s[12:76]
    repeat_chars = set()
    for i in range(len(segment)):
        if segment[i] in segment[i + 1:]:
            repeat_chars.add(segment[i])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)