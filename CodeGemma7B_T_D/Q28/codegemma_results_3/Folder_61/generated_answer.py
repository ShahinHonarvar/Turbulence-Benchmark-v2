def return_nth_smallest_ascii(str1):
    return sorted([x for x in str1 if str1.index(x) in range(10)])[9]