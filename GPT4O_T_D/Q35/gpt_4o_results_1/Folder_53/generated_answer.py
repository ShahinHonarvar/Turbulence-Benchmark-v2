def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    substring = s[201:202]
    counts = {char: substring.count(char) for char in set(substring)}
    remove_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in remove_chars))