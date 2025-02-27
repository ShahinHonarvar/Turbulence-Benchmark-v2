def filter_chars(s: str) -> str:
    filtered_chars = []
    for i in range(len(s)):
        if not (63 <= i <= 84 and 'E' <= s[i] <= '~'):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)