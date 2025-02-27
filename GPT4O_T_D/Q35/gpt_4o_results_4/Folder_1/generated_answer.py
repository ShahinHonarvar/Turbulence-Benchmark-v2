def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    start, end = (18, 88)
    section = s[start:end]
    counts = {}
    for char in section:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char in chars_to_remove and start <= s.index(char) < end:
            continue
        result.append(char)
    return ''.join(result)