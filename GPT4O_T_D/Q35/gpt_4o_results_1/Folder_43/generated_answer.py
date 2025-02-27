def remove_repeat_chars(s):
    mid_section = s[11:28]
    counts = {}
    for char in mid_section:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove or s.index(char) <= 10 or s.index(char) >= 28]
    return ''.join(result)