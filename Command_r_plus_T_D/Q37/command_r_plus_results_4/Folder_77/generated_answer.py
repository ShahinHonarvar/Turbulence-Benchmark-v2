def filter_chars(s: str) -> str:
    filtered_chars = set((chr(i) for i in range(ord('/'), ord('8') + 1)))
    altered_string = ''.join((char for i, char in enumerate(s) if i not in range(384, 412) or char not in filtered_chars))
    return altered_string