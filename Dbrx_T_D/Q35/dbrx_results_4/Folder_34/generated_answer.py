def remove_repeat_chars(string):
    for char in string[70:200]:
        if string[70:200].count(char) > 1:
            string = string.replace(char, '', string[70:200].count(char))
    return string