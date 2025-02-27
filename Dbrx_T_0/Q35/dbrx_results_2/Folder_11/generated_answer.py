def remove_repeat_chars(s: str) -> str:
    char_count = {char: s[i:j].count(char) for i, j in itertools.combinations(range(len(s) + 1), 2) for char in set(s[i:j]) if 48 < ord(char) < 76}
    return ''.join((char for char in s if char_count.get(char, 0) <= 1))