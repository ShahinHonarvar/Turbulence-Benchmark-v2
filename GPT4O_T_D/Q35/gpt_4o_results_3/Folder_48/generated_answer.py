def remove_repeat_chars(s):
    if len(s) <= 410:
        return s
    substring_counts = {}
    for char in s[410:502]:
        if char in substring_counts:
            substring_counts[char] += 1
        else:
            substring_counts[char] = 1
    repeated_chars = {char for char, count in substring_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)