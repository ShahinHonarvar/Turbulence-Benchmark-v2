def remove_repeat_chars(s):
    count = {}
    repeated = set()
    for i in range(463, 995):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
            if count[char] > 1:
                repeated.add(char)
    result = ''
    for char in s:
        if char not in repeated:
            result += char
    return result