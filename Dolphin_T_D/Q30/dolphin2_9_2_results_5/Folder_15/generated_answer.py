def insert_before_character(s):
    result = ''
    for i in s:
        if i == 'o':
            result += 'o' + i
        else:
            result += i
    return result + s[-1] if result != s else result + 'o' + s[-1]