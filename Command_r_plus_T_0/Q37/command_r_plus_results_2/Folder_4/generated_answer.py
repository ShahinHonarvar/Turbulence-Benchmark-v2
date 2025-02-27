def filter_chars(s: str) -> str:
    chars_to_remove = set(s[19:34]) & set('S"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMN')
    return ''.join((c for c in s if c not in chars_to_remove))