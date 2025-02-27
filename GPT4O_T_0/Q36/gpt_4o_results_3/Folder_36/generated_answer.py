def filter_chars(s):
    if len(s) <= 284:
        return s
    chars_to_remove = {chr(i) for i in range(ord('m'), ord('t'))}
    filtered_part = ''.join((c for c in s[284:484] if c not in chars_to_remove))
    return s[:284] + filtered_part + s[484:]