def remove_repeat_chars(string):
    for i in range(86, 90):
        for j in range(i):
            if string[j] == string[i]:
                string = string[:j] + string[j + 1:]
    return string