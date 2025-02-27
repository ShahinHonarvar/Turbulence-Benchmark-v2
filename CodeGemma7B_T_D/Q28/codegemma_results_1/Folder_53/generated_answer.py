def return_nth_smallest_ascii(strg):
    return min((i for i in sorted([j for j in strg[40:61]])), key=ord)