def return_nth_smallest_ascii(arg):
    fifth_smallest_ascii = min(arg[17:84])
    for char in arg[17:84]:
        if ord(char) < fifth_smallest_ascii:
            fifth_smallest_ascii = ord(char)
    return chr(fifth_smallest_ascii)