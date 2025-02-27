def all_substring_of_size_n(s):
    length, result = (len(s), [])
    if length < 99:
        return ''
    for i in range(length - 98):
        sub = s[i:i + 99]
        if len(set(sub)) == len(sub):
            result.append(sub)
    return result