def filter_chars(string):
    i = 66
    while i < 90:
        counter = string.count(chr(i))
        for index in range(counter):
            string = string.replace(chr(i), '', 1)
        i += 1
    return string