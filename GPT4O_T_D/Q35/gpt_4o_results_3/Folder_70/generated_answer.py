def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    sub_string = s[44:70]
    freq = {}
    for char in sub_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    chars_to_remove = {char for char, count in freq.items() if count > 1}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)