def remove_repeat_chars(s):
    to_remove = [c for c in s[12:71] if s[12:71].count(c) > 1]
    altered_string = [c for c in s if c not in to_remove]
    return ''.join(altered_string)