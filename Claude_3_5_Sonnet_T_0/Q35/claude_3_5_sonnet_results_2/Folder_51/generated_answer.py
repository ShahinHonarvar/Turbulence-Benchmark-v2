def remove_repeat_chars(s):
    target_substring = s[7:9]
    repeat_chars = set((c for c in target_substring if target_substring.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))