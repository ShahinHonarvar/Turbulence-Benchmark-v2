def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    sub_str = s[43:87]
    counts = {}
    for char in sub_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = {char for char in counts if counts[char] > 1}
    result = ''.join((char for char in s if char not in to_remove or not 43 <= s.index(char) <= 86))
    return result