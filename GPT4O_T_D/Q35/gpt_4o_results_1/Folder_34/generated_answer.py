def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub_str = s[71:200]
    char_count = {}
    for char in sub_str:
        char_count[char] = char_count.get(char, 0) + 1
    removal_set = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in removal_set or not 71 < s.index(char) < 200]
    return ''.join(result)