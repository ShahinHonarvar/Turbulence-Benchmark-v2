def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(27, 96):
        if chr(i) in s:
            chars_to_remove.add(chr(i))
    for char in chars_to_remove:
        while True:
            s = s.replace(char, '', 1)
            if char not in s:
                break
    return s