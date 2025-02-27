def filter_chars(s: str) -> str:
    start_index = 58
    end_index = 82
    filtered_chars = []
    for i in range(len(s)):
        if i >= start_index and i < end_index:
            if s[i] > 'F' and s[i] < 'O':
                continue
        filtered_chars.append(s[i])
    return ''.join(filtered_chars)