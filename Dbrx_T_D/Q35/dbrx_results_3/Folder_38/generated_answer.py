def remove_repeat_chars(s):
    chars = {}
    for i in range(len(s)):
        if i >= 36 and i < 85:
            if s[i] in chars:
                chars[s[i]].append(i)
            else:
                chars[s[i]] = [i]
        elif s[i] not in chars:
            chars[s[i]] = [i]
    result = ''
    for c in chars:
        if len(chars[c]) == 1:
            result += c
        else:
            start = min(chars[c])
            end = max(chars[c])
            result += s[start:end + 1]
    return result