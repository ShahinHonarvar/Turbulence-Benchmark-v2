def remove_repeat_chars(str):
    seen = {}
    result = []
    for char in str:
        if char not in seen or seen[char] + 1 < 4:
            seen[char] = seen.get(char, 0) + 1
            result.append(char)
    return ''.join(result)