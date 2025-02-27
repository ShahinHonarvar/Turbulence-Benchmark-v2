def remove_repeat_chars(s: str) -> str:
    char_count = {char: s[i:j].count(char) for i, j in itertools.zip_longest(range(48, 76), range(49, 77)) for char in set(s[i:j])}
    return ''.join((char for char in s if char_count.get(char, 0) <= 1))