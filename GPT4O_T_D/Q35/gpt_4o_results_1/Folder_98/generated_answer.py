def remove_repeat_chars(s):
    to_remove = set()
    for char in s[1:7]:
        if s[1:7].count(char) > 1:
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))