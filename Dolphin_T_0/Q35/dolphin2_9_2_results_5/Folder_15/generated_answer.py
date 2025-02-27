def remove_repeat_chars(string):
    seen = set()
    result = ''
    for char in string:
        if char not in seen and string.count(char) <= 1:
            result += char
            seen.add(char)
    return result