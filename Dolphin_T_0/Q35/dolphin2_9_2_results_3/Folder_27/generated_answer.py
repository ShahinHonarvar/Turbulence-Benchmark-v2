def remove_repeat_chars(s):
    to_remove = set()
    for i in range(86, 89):
        chars = s[i]
        if chars in s[:i] or chars in s[i + 1:]:
            to_remove.add(chars)
    return ''.join((ch for ch in s if ch not in to_remove))