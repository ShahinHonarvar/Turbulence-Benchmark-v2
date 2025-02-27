def remove_repeat_chars(s):
    counts = {}
    for char in s[34:69]:
        counts[char] = counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))