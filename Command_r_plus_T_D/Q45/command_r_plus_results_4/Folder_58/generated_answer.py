def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_str = ''.join(filter(english_letters.__contains__, s[:7]))
    if len(filtered_str) < 6:
        return set()
    result = set()
    for i in range(len(filtered_str) - 5):
        window = filtered_str[i:i + 6]
        if window == window[::-1]:
            result.add(window)
    return result