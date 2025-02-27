def remove_repeat_chars(s):
    start, end = (331, 543)
    counts = {}
    for char in s[start:end]:
        counts[char] = counts.get(char, 0) + 1
    result = []
    for i, char in enumerate(s):
        if not (start < i < end and counts.get(char, 0) > 1):
            result.append(char)
    return ''.join(result)