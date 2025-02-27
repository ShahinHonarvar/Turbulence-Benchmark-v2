def remove_repeat_chars(s):
    freq = {}
    chars = set()
    for i in range(6, 10):
        freq[s[i]] = freq.get(s[i], 0) + 1
        if freq[s[i]] > 1:
            chars.add(s[i])
    result = ''
    for char in s:
        if char not in chars:
            result += char
    return result