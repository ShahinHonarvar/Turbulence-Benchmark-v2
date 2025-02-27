def remove_repeat_chars(s):
    freq = {}
    for i in range(20, 43):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    result = ''
    for i in s:
        if i not in freq or freq[i] == 1:
            result += i
    return result