def remove_repeat_chars(s):
    substring = s[463:995]
    repeated_chars = set()
    for i in range(len(substring)):
        if substring.count(substring[i]) > 1:
            repeated_chars.add(substring[i])
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)