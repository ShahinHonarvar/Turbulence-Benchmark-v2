def remove_repeat_chars(string):
    chars = set()
    result = ''
    for char in string[1:6]:
        if char in chars:
            while char in result:
                result = result[result.index(char) + 1:]
        else:
            chars.add(char)
            result += char
    return result + string[6:]