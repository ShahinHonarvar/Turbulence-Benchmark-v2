def remove_repeat_chars(s):
    substring = s[58:85]
    counts = {}
    for char in substring:
        counts[char] = counts.get(char, 0) + 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result