def filter_chars(s: str) -> str:
    start, end = (171, 636)
    threshold_lower, threshold_upper = (ord('c'), ord('s'))
    filtered_chars = []
    for i, char in enumerate(s):
        if start <= i < end:
            if not threshold_lower < ord(char) < threshold_upper:
                filtered_chars.append(char)
        elif i >= end:
            filtered_chars.append(char)
    return ''.join(filtered_chars)