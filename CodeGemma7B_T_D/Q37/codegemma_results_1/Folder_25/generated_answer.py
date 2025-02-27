def filter_chars(string):
    for i in range(31, 39):
        for j in range(len(string)):
            if string[j] == chr(i):
                string = string[:j] + string[j + 1:]
                j -= 1
    return string