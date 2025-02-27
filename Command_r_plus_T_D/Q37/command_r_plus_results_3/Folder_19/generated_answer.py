def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if i in range(35, 90) and char in 'EFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst':
            continue
        result.append(char)
    return ''.join(result)