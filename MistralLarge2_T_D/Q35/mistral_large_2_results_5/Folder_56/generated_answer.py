def remove_repeat_chars(s):
    indices = set(range(7, 10))
    count = {}
    for i in range(len(s)):
        if i not in indices:
            count[s[i]] = count.get(s[i], 0) + 1
    result = [char for char in s if count.get(char, 0) <= 1]
    return ''.join(result)