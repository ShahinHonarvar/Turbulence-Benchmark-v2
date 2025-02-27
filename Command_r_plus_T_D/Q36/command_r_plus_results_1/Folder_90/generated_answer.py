def filter_chars(s: str) -> str:
    result = []
    exclude_range = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    for idx, char in enumerate(s):
        if 344 <= idx < 874 and char in exclude_range:
            continue
        result.append(char)
    return ''.join(result)