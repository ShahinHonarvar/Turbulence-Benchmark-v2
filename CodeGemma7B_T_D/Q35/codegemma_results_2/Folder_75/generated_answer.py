def remove_repeat_chars(txt):
    seen = set()
    new_txt = []
    for i, char in enumerate(txt):
        if 20 <= i < 51 and char in seen:
            continue
        seen.add(char)
        new_txt.append(char)
    return ''.join(new_txt)