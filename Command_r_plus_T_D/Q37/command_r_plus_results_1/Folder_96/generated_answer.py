def filter_chars(s: str) -> str:
    chars_to_remove = set(s[86:93]) & set('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO')
    return ''.join((ch for ch in s if ch not in chars_to_remove))