from collections import defaultdict

def remove_repeat_chars(s):
    d = defaultdict(list)
    for i, c in enumerate(s[38:52]):
        d[c].append(i)
    to_remove = set()
    for char, indices in d.items():
        if len(indices) > 1:
            to_remove.update(indices[1:])
    return ''.join((c for i, c in enumerate(s) if i not in to_remove))