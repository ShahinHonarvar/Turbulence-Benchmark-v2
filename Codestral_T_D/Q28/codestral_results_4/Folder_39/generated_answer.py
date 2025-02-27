def return_nth_smallest_ascii(s):
    characters = sorted(s[1:67], key=ord)[7]
    return characters