def remove_repeat_chars(string):
    chars = {}
    result = ''
    for i in range(125, 825):
        if i < len(string):
            char = string[i]
            if char in chars:
                chars[char] += 1
                if chars[char] > 1:
                    result = result.replace(char, '')
            else:
                chars[char] = 1
                result += char
    return result