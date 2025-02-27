from math import sqrt

def composite_nums_between_indices(list1):
    s = set()
    for i in range(13, 69):
        if list1[i] % 2 == 0 and list1[i] != 2:
            s.add(list1[i])
        for j in range(3, int(sqrt(list1[i])) + 1, 2):
            if list1[i] % j == 0:
                s.add(list1[i])
                break
    return s