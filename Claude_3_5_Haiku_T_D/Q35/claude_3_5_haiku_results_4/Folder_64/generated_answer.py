def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    freq = {}
    for i in range(1, 5):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    repeat_chars = [char for char, count in freq.items() if count > 1]
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result