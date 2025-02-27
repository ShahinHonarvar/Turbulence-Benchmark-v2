def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    substring = s[21:200]
    char_counts = {}
    for char in substring:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    to_remove = {char for char, count in char_counts.items() if count > 1}
    result = []
    for i in range(len(s)):
        if i <= 20 or i >= 200 or s[i] not in to_remove:
            result.append(s[i])
    return ''.join(result)