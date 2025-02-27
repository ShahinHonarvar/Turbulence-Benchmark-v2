def remove_repeat_chars(s):
    chars = [c for c in s if c in string.printable[32:99]]
    counts = {c: [i for i, c2 in enumerate(s) if c == c2] for c in set(chars)}
    to_remove = [k for k, v in counts.items() if len(v) > 1]
    return ''.join((c for c in s if c not in to_remove))