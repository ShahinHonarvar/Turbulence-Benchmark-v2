def remove_repeat_chars(s):
    count = {}
    to_remove = set()
    result = []
    for i, char in enumerate(s):
        if 0 < i < 8:
            if char in count:
                to_remove.add(char)
            else:
                count[char] = 1
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)