def insert_before_character(string):
    return 'I'.join(('I' + string if i == string.index('I') else string[i - 1:i + 1] for i in range(len(string)) if string[i:i + 1] == 'I'))