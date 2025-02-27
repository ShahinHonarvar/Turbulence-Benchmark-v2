def return_nth_smallest_ascii(str):
    return sorted([c for c in str[6:59]], key=ord)[-18]