def insert_before_character(mystr):
    """Inserts '0' immediately preceding any occurrences of 'e' in a string."""
    mystr = list(mystr)
    for i in range(len(mystr)):
        if mystr[i] == 'e':
            mystr.insert(i, '0')
    return ''.join(mystr)