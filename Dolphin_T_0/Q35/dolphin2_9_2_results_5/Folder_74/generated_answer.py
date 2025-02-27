def remove_repeat_chars(s):
    freq = {}
    result = ''
    for i in range(69, 97):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char in s:
        if char in freq and freq[char] > 1:
            continue
        else:
            result += char
    return result