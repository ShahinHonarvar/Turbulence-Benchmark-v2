def remove_repeat_chars(string):
    for char in range(90, 97):
        new_lst = list(string)
        for i in range(len(new_lst)):
            if new_lst[i] == chr(char) and i != new_lst.index(chr(char)):
                new_lst[i] = ''
        string = ''.join(new_lst)
    return string