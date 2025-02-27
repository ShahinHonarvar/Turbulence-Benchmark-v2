def remove_repeat_chars(s):
    counts = {char: s[1:5].count(char) for char in set(s[1:5])}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))