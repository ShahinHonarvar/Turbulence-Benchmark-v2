def remove_repeat_chars(s):
    count = {}
    result = ''
    for char in s:
        if 56 <= s.index(char) <= 90:
            if char not in count:
                count[char] = 1
                result += char
            elif count[char] == 1:
                result += char
            elif count[char] > 1:
                continue
        else:
            result += char
    return result