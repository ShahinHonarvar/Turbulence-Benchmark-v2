def remove_repeat_chars(s):

    def count_chars(sub_str):
        char_count = {}
        for char in sub_str:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    if len(s) <= 355:
        return s
    in_range_substring = s[356:988]
    char_count = count_chars(in_range_substring)
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)