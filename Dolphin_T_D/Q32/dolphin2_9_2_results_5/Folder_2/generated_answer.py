def insert_after_character(aStr):
    newStr = ''
    for i in aStr:
        newStr += i
        if i == 'C':
            newStr += 'Z'
    return newStr