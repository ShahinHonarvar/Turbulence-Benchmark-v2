def filter_chars(s: str) -> str:
    start_index = 587
    end_index = 648
    filtered_chars = ''
    for i in range(len(s)):
        if i >= start_index and i < end_index:
            if s[i] > ',' and s[i] < 'c':
                filtered_chars += s[i]
        else:
            filtered_chars += s[i]
    return filtered_chars