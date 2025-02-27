def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('!') + 1, ord('A'))}
    return s[:12] + ''.join((c for c in s[12:46] if c not in chars_to_remove)) + s[46:]