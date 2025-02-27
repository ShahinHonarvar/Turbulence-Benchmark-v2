def filter_chars(s: str) -> str:
    start, end = (51, 76)
    return ''.join((c for i, c in enumerate(s) if i < start or i >= end or (not '5' < c < 'f'))) if len(s) >= 76 else s