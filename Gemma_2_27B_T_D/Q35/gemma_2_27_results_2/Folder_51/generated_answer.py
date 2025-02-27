def remove_repeat_chars(text):
    seen = set()
    remove_chars = set()
    for i in range(len(text)):
        if 6 <= i < 9:
            if text[i] in seen:
                remove_chars.add(text[i])
            else:
                seen.add(text[i])
    result = ''.join([c for c in text if c not in remove_chars])
    return result