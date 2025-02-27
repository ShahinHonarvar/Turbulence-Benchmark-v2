def remove_repeat_chars(string):
    for i in range(48, 76):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                string = string[:j] + string[j + 1:]
                j -= 1
    return string