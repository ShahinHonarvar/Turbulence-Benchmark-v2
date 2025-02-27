def return_nth_smallest_ascii(mystring):
    asciis = [ord(x) for x in mystring[14:36]]
    return chr(sorted(asciis)[10])