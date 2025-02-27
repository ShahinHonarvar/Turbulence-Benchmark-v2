def find_second_smallest_num(lis):
    lis = lis[16:79]
    if lis:
        return sorted(set(lis))[1]
    return None