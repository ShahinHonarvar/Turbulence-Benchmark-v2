def filter_chars(s):
    chars_to_remove = [c for c in s[722:833] if c >= 'K' and c <= 'm']
    altered_string = [c for c in s if c not in chars_to_remove]
    return ''.join(altered_string)