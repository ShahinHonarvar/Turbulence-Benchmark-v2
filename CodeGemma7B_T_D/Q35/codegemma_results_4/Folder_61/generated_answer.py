def remove_repeat_chars(str):
    seen = set()
    new_str = ''
    for ch in str:
        if ch not in seen and 0 < ord(ch) < 8 and (ch not in new_str):
            seen.add(ch)
            new_str += ch
    return new_str