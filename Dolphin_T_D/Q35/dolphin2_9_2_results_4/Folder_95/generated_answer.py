def remove_repeat_chars(string):
    count = {}
    for char in string:
        if 32 <= ord(char) <= 99:
            count[char] = count.get(char, 0) + 1
    for char, freq in count.items():
        if freq > 1:
            string = string.replace(char, '')
    return string