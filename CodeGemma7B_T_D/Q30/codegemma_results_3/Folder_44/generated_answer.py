def insert_before_character(string):
    a = string.rfind('g')
    b = string.rindex('g')
    c = string.rindex('g', 0, a)
    if b != c:
        return string[:c + 1] + 'M' + string[c + 1:a] + 'M' + string[a:]
    else:
        return string[:a] + 'M' + string[a:]