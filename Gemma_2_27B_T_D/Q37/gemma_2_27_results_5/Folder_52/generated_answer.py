def filter_chars(string: str) -> str:
    result = list(string)
    for i in range(54, 84):
        if i < len(string) and string[i] >= 'j' and (string[i] <= 'v'):
            char = string[i]
            result = [c for c in result if c != char]
    return ''.join(result)