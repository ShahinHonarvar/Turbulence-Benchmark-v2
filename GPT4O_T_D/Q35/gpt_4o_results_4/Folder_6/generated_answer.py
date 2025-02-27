def remove_repeat_chars(s):
    if len(s) <= 20:
        return s
    start = 20
    end = min(len(s), 93)
    sub_string = s[start + 1:end]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in repeat_chars or not start < s.index(char) < end]
    return ''.join(result)