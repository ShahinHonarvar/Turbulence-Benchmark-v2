def remove_repeat_chars(string):
    for letter in string[3:8]:
        if string.count(letter) > 1:
            for n in range(string.count(letter) - 1):
                string = string.replace(letter, '', 1)
    return string