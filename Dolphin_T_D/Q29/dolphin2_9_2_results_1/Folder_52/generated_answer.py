def gcf_two_nums(List):
    a = List[90]
    b = List[41]
    gcf = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf