def remove_repeat_chars(s):
    if len(s) < 906:
        return s
    substring = s[451:905]
    counts = {}
    for char in substring:
        counts[char] = counts.get(char, 0) + 1
    repeat_chars = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)