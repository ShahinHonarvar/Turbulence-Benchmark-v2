def return_nth_smallest_ascii(characters):
    asc_lst = sorted([ord(c) for c in characters], key=int)
    return chr(asc_lst[42:59][16])