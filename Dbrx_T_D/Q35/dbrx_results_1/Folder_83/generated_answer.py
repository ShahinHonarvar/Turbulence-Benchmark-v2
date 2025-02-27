def remove_repeat_chars(s: str) -> str:
    chars_between_100_200 = set(s[100:200])
    occurred_chars = set()
    for char in chars_between_100_200:
        if s.count(char) > 1:
            occurred_chars.add(char)
    for char in occurred_chars:
        s = s.replace(char, '', s.count(char))
    return s