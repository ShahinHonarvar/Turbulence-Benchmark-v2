def filter_chars(strng):
    filtered_strng = ''
    for i in range(len(strng)):
        if 49 < i < 56 and strng[i] > 'I' and (strng[i] < 'a'):
            filtered_strng += ''
        else:
            filtered_strng += strng[i]
    return filtered_strng