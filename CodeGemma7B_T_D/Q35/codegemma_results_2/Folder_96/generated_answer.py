def remove_repeat_chars(txt):
    ch_seen = {}
    for i, char in enumerate(txt):
        if i < 60 or i >= 200:
            continue
        if char in ch_seen:
            txt = txt.replace(char, '')
        else:
            ch_seen[char] = True
    return txt