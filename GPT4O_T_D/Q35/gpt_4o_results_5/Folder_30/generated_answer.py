def remove_repeat_chars(s):
    start = 23
    end = 24
    chars_to_remove = set()
    for i in range(start + 1, end):
        if s[i] in s[start + 1:end]:
            if s[start + 1:end].count(s[i]) > 1:
                chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))