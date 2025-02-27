def filter_chars(s: str) -> str:
    return ''.join((c for c in s[:502] + s[946:] if s[502:946].count(c) == 0 and 'W' < c < 'y'))