def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('G'), ord('O'))}
    filtered_chars = s[:59] + ''.join((c for c in s[59:82] if c not in chars_to_remove)) + s[82:]
    return filtered_chars