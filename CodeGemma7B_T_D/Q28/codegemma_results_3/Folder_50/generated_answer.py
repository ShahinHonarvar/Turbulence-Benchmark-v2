def return_nth_smallest_ascii(mystring):
    return sorted([x for x in mystring[25:88] if ord(x) >= 65 and ord(x) <= 90])[10]