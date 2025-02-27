def insert_after_character(s: str) -> str:
    res = ''
    for ch in s:
        res += ch
        if ch == '9':
            res += 'h'
    return res