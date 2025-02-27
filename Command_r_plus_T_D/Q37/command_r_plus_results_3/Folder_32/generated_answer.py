def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[23:90] if 'w' <= ch <= '{'))
    result = []
    for ch in s:
        if ch not in chars_to_remove:
            result.append(ch)
    return ''.join(result)