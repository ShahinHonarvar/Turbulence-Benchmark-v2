def remove_repeat_chars(string):
    seen_chars = set()
    kept_chars = []
    for i in range(len(string)):
        if i >= 10 and i < 28 and (string[i] in seen_chars):
            continue
        if i >= 10 and i < 28:
            seen_chars.add(string[i])
        kept_chars.append(string[i])
    return ''.join(kept_chars)