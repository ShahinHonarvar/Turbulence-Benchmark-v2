def remove_repeat_chars(s):
    to_remove = [c for c in s[35:64] if s[35:64].count(c) > 1]
    result = [c for c in s if c not in to_remove]
    return ''.join(result)