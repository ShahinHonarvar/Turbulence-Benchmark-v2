def filter_chars(s: str) -> str:
    filter_range = range(300, 419)
    filter_chars = [chr(i) for i in range(ord('9') + 1, ord('P'))]
    filtered_s = []
    for i, char in enumerate(s):
        if i in filter_range and char in filter_chars:
            continue
        filtered_s.append(char)
    return ''.join(filtered_s)