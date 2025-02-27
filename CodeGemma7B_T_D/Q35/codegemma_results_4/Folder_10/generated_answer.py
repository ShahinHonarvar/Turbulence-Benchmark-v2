def remove_repeat_chars(str):
    result = str[:36]
    for i in range(36, 54):
        chars = defaultdict(int)
        for char in result + str[i:]:
            chars[char] += 1
        for char, count in chars.items():
            if count > 1:
                result += char
    return result + str[54:]