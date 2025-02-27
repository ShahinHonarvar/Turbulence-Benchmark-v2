def remove_repeat_chars(s: str) -> str:
    to_remove = set()
    for i in range(32, 99):
        if s.count(chr(i)) > 1:
            to_remove.add(chr(i))
    return ''.join((c for c in s if c not in to_remove))