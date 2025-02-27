def return_nth_smallest_ascii(string):
    res = sorted([ord(s) for s in string[24:72]])[7]
    return chr(res)