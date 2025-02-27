def return_nth_smallest_ascii(s):
    temp = sorted([s[i] for i in range(36, 80)])
    return temp[11]