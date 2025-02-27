def remove_repeat_chars(text):
    seen = set()
    to_remove = set()
    for i in range(44, 91):
        if text[i] in seen:
            to_remove.add(text[i])
        else:
            seen.add(text[i])
    result = ''.join((c for c in text if c not in to_remove))
    return result