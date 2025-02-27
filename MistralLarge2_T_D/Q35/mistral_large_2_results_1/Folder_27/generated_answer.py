def remove_repeat_chars(s):
    substring = s[86:89]
    counts = {char: substring.count(char) for char in substring}
    return ''.join((char for char in s if counts.get(char, 0) <= 1))