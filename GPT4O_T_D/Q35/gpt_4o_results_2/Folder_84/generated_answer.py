def remove_repeat_chars(s):
    substr = s[33:44]
    counts = {char: substr.count(char) for char in set(substr)}
    to_remove = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)