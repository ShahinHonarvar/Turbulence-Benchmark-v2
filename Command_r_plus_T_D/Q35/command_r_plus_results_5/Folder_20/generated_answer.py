def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(27, 96):
        if s.count(chr(i)) > 1:
            repeat_chars.add(chr(i))
    return ''.join((c for c in s if c not in repeat_chars))