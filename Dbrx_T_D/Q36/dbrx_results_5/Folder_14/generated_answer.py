def filter_chars(s: str) -> str:
    start_index = 41
    end_index = 56
    filter_range = set(range(ord('Z') + 1, ord('c')))
    return ''.join((c for i, c in enumerate(s) if i < start_index or i >= end_index or ord(c) not in filter_range))