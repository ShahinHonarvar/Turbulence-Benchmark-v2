def remove_repeat_chars(string):
    for i in range(44, 67):
        temp_str = list(string[i])
        if string[i] in string[44:67] and temp_str.count(string[i]) > 1:
            while temp_str.count(string[i]) > 1:
                temp_str.remove(string[i])
            if len(temp_str) == 1:
                string = string[:i] + temp_str[0] + string[i + 1:]
            else:
                string = string[:i] + ''.join(temp_str) + string[i + 1:]
    return string