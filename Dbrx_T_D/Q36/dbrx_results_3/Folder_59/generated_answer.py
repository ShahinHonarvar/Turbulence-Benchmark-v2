def filter_chars(s: str) -> str:
    start_index = 3
    end_index = 8
    lower_bound = ord('?') + 1
    upper_bound = ord('k')
    chars_to_remove = [c for c in s if lower_bound <= ord(c) < upper_bound and start_index < s.index(c) < end_index]
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s