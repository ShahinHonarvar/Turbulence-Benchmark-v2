def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 669 or i >= 888 or ((c <= 'B' or c >= 'Y') and c not in s[669:888])))