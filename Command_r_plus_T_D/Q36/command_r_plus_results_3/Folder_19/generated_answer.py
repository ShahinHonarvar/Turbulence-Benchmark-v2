def filter_chars(s: str) -> str:
    filter_range = range(77, 87)
    filter_chars = [chr(i) for i in range(59, 114) if i not in range(ord(s[i]), ord(s[i]) + 1)]
    for i in filter_range:
        s = s.replace(s[i], '', s.count(s[i]))
    return s