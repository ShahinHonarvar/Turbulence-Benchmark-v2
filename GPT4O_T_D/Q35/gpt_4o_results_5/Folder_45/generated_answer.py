def remove_repeat_chars(s):
    if len(s) <= 41:
        return s
    substring = s[41:200]
    counts = {char: substring.count(char) for char in set(substring)}
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char in chars_to_remove and 41 < s.index(char) < 200:
            continue
        result.append(char)
    return ''.join(result)