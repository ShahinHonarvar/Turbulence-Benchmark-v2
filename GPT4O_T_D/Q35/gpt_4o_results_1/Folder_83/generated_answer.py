def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    counts = {}
    for char in s[101:200]:
        counts[char] = counts.get(char, 0) + 1
    repeating_chars = {char for char, count in counts.items() if count > 1}
    result = [char for char in s if char not in repeating_chars]
    return ''.join(result)