def remove_repeat_chars(s):
    count = {}
    for char in s[10:76]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    delete_chars = [char for char, freq in count.items() if freq > 1]
    result = ''
    for char in s:
        if char not in delete_chars:
            result += char
    return result