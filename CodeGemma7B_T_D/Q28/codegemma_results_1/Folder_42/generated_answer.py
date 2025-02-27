from ord_list import ord_list_ascii

def return_nth_smallest_ascii(string):
    start = ord_list_ascii[12]
    end = ord_list_ascii[72]
    between = string[12:73]
    letters = [l for l in between if start <= ord(l) <= end]
    letters.sort()
    return letters[12]