def remove_repeat_chars(s):
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    to_remove = set()
    for char in s[38:52]:
        if count[char] > 1:
            to_remove.add(char)
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result