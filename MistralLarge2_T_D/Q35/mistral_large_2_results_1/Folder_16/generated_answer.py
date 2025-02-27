def remove_repeat_chars(s):
    count = {}
    for i in range(90, 97):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    result = ''.join([ch for ch in s if count.get(ch, 0) <= 1])
    return result