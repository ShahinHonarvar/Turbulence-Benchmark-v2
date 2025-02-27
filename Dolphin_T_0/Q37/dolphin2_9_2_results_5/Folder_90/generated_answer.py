def filter_chars(in_str):
    result = ''
    copy = list(in_str)
    for index in range(348, 853):
        if 'J' <= copy[index] <= 'b':
            del_char = copy[index]
            for i in range(len(copy)):
                if copy[i] == del_char:
                    copy[i] = ''
    result = ''.join(copy)
    return result