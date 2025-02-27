def filter_chars(s: str) -> str:
    filter_range = range(77, 87)
    filter_chars = [chr(i) for i in range(59, 114) if i != 59 and i != 114]
    filtered_s = s
    for idx in filter_range:
        if s[idx] in filter_chars:
            filtered_s = filtered_s.replace(s[idx], '')
    return filtered_s