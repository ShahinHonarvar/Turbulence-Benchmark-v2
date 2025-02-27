def return_nth_smallest_ascii(string):
    list_ascii = []
    for i in range(len(string)):
        if i >= 0 and i <= 4:
            list_ascii.append(ord(string[i]))
    list_ascii.sort()
    return chr(list_ascii[3])