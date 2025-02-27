def filter_chars(input_string: str) -> str:
    char_set = set(input_string[86:93])
    filtered_set = {c for c in char_set if '!' <= c <= 's'}
    return ''.join((c for c in input_string if c not in filtered_set))