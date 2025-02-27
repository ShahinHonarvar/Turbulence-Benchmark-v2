def remove_repeat_chars(s):
    freq_map = {}
    for char in s[18:60]:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    result = ''
    for char in s:
        if char in freq_map and freq_map[char] <= 1 or char not in freq_map:
            result += char
    return result