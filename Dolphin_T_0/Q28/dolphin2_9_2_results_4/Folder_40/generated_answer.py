def return_nth_smallest_ascii(string):
    values = [(string[i], ord(string[i])) for i in range(5)]
    values.sort(key=lambda x: x[1])
    return values[4][0]