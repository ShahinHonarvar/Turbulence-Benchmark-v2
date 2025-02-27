def remove_repeat_chars(s):
    seen = set()
    to_remove = set()
    for i in range(1, len(s) - 1):
        if s[i] in seen:
            to_remove.add(s[i])
        seen.add(s[i])
    return ''.join([char for char in s if char not in to_remove])