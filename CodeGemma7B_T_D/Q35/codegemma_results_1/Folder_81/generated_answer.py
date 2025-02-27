def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, char in enumerate(s):
        if i < 20 or i >= 200:
            if char not in seen or seen[char] < 1:
                result.append(char)
                seen[char] = 1
    return ''.join(result)