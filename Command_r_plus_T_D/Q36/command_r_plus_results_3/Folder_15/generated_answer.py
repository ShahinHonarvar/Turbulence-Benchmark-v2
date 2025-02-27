def filter_chars(s: str) -> str:
    filter_range = range(2, 7)
    filter_chars = [char for char in s if 'h' < char < 'k']
    result = []
    index = 0
    for char in s:
        if index in filter_range and char in filter_chars:
            continue
        result.append(char)
        index += 1
    return ''.join(result)