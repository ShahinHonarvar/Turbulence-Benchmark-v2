def remove_repeat_chars(s):
    count = {}
    for i in range(450, 905):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    result = ''.join([char for char in s if count.get(char, 0) <= 1])
    return result