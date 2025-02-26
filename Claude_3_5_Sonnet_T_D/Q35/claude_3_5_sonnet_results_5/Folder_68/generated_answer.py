def remove_repeat_chars(s):
    counts = {}
    result = []
    for i, char in enumerate(s):
        if 0 < i < 9:
            counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)