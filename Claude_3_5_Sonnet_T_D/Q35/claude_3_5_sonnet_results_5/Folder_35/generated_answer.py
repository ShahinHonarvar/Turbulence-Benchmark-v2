def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    target_section = s[77:84]
    repeats = set((char for char in target_section if target_section.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if char not in repeats or (i < 77 or i >= 84):
            result.append(char)
    return ''.join(result)