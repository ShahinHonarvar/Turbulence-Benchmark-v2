def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    mid_section = s[21:35]
    seen = {}
    for char in mid_section:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    chars_to_remove = {char for char, count in seen.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 20 or s.index(char) >= 35))