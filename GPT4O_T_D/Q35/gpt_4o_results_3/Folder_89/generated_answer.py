def remove_repeat_chars(s):
    count = {}
    for c in s[56:84]:
        if c not in count:
            count[c] = 0
        count[c] += 1
    to_remove = {c for c, n in count.items() if n > 1}
    return ''.join((c for c in s if c not in to_remove or s.index(c) <= 55 or s.index(c) >= 84))