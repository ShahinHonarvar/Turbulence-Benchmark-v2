def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    substring = s[71:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    seen_chars = set()
    for char in s:
        if char in repeated_chars and 71 <= s.index(char) <= 200:
            continue
        if char not in seen_chars or s.index(char) < 71 or s.index(char) > 200:
            result.append(char)
            seen_chars.add(char)
    return ''.join(result)