def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 259 <= idx <= 502 and char in [',', '.', '/', '0', '1', '2', '3']:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)