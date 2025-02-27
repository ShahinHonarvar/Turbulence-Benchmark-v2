def remove_repeat_chars(s):
    freq_map = {}
    new_string = ''
    for i, char in enumerate(s):
        if 20 <= i <= 51:
            freq_map[char] = freq_map.get(char, 0) + 1
    for char in s:
        if char not in freq_map or freq_map[char] == 1:
            new_string += char
    return new_string