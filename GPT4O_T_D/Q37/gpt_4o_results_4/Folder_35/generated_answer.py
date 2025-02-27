def filter_chars(s):
    to_remove = set(s[155:404])
    filtered_remove = {ch for ch in to_remove if '(' <= ch <= ']'}
    return ''.join((ch for ch in s if ch not in filtered_remove))