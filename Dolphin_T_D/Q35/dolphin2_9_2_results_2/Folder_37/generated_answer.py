def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, ch in enumerate(s):
        if i < 2 or i > 7 or ch not in seen:
            result += ch
            seen.add(ch)
    return result