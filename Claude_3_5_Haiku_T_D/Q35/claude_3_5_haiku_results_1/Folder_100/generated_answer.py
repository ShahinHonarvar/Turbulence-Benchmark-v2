def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    segment = s[45:78]
    chars_to_remove = set()
    for i in range(len(segment)):
        for j in range(i + 1, len(segment)):
            if segment[i] == segment[j] and segment[i] not in chars_to_remove:
                chars_to_remove.add(segment[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result