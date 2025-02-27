def remove_repeat_chars(s):
    char_count = {}
    for i, c in enumerate(s[35:69]):
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    repeat_chars = {c for c in char_count if char_count[c] > 1}
    result = [c for c in s if c not in repeat_chars]
    return ''.join(result)