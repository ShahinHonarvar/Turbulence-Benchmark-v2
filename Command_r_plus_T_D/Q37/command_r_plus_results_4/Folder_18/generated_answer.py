def filter_chars(s: str) -> str:
    filtered_chars = set((chr(i) for i in range(ord('-'), ord('D') + 1)))
    altered_string = []
    for i, char in enumerate(s):
        if i in range(770, 971) and char in filtered_chars:
            continue
        altered_string.append(char)
    return ''.join(altered_string)