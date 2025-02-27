def return_nth_smallest_ascii(str):
    return sorted([i for i in str if str.index(i) >= 0 and str.index(i) <= 87])[13]