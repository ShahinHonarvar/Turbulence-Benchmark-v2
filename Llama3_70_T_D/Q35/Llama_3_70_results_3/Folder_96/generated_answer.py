def remove_repeat_chars(s):
    count = {}
    for i in range(60, 200):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    remove_chars = [char for char, freq in count.items() if freq > 1]
    result = ''
    for char in s:
        if char not in remove_chars:
            result += char
    return result