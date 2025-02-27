def return_nth_smallest_ascii(string):
    list_of_ascii = [ord(i) for i in string[62:84]]
    list_of_ascii.sort()
    return chr(list_of_ascii[8])