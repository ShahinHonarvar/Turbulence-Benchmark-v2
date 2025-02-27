def remove_repeat_chars(s):
    substring = s[33:78]
    counts = {char: substring.count(char) for char in set(substring)}
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))