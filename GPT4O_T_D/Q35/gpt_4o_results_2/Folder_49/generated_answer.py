def remove_repeat_chars(s):
    to_remove = set()
    for char in s[91:200]:
        if s[91:200].count(char) > 1:
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))