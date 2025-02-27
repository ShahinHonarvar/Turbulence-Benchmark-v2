def remove_repeat_chars(s):
    substring = s[331:543]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in repeated_chars or char not in s[331:543]]
    return ''.join(result)