def remove_repeat_chars(s):
    count = {}
    for char in s[69:99]:
        count[char] = count.get(char, 0) + 1
    to_remove = {char for char in count if count[char] > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result