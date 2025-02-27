def remove_repeat_chars(s):
    start, end = (103, 802)
    char_count = {}
    for i in range(start, end):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in repeated_chars]
    return ''.join(result)