def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    segment = s[44:70]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = []
    seen_chars = set()
    for char in s:
        if char in repeated_chars and char not in seen_chars:
            seen_chars.add(char)
        elif char not in repeated_chars or (char in repeated_chars and char in seen_chars):
            result.append(char)
    return ''.join(result)