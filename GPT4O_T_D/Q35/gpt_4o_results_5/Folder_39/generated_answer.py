def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    substring = s[45:91]
    counts = {}
    for char in substring:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)