def remove_repeat_chars(s):
    if len(s) <= 80:
        return s
    sub = s[81:200]
    counts = {}
    for char in sub:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)