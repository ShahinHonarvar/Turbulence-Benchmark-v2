def remove_repeat_chars(s):
    counter = {}
    for c in s[49:76]:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    chars_to_remove = {c for c, count in counter.items() if count > 1}
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result