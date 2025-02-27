def remove_repeat_chars(s):
    new_string = ''
    counter = {}
    for char in s:
        if ord(char) in range(27, 96, 1) and char not in new_string:
            counter[char] = 1
            new_string += char
        elif ord(char) in range(27, 96, 1) and char in counter and (counter[char] == 1):
            new_string = new_string.replace(char, '')
            counter[char] += 1
    return new_string