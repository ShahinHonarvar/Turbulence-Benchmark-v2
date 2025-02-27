def remove_repeat_chars(s):
    count = {}
    for idx in range(45, 48):
        if s[idx] in count:
            count[s[idx]] += 1
        else:
            count[s[idx]] = 1
    result = ''.join((char for char in s if count.get(char, 0) <= 1))
    return result