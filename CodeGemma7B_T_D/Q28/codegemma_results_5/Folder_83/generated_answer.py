def return_nth_smallest_ascii(strr):
    charr = sorted([c for c in strr[30:71] if c.isalpha()])
    return charr[14]