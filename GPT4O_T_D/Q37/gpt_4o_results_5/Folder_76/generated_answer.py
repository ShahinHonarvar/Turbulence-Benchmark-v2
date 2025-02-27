def filter_chars(s):
    filtered_chars = {chr(i) for i in range(ord('M'), ord('v') + 1)}
    chars_to_remove = {s[i] for i in range(379, min(899, len(s))) if s[i] in filtered_chars}
    return ''.join((c for c in s if c not in chars_to_remove))