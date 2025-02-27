def filter_chars(astring):
    strlist = list(astring)
    for i in range(18, 31):
        if astring[i] > 'H' and astring[i] < '|':
            strlist[i] = ' '
    return ''.join(strlist)