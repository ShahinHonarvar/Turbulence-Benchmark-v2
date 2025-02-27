def return_nth_smallest_ascii(string):
    values = []
    for i in range(60, 84):
        if string[i].isalpha():
            values.append(ord(string[i]))
    values.sort()
    return chr(values[13])