def remove_repeat_chars(s):
    counts = {}
    result = []
    for i, char in enumerate(s):
        if 10 < i < 76:
            counts[char] = counts.get(char, 0) + 1
    for i, char in enumerate(s):
        if 10 < i < 76 and counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)