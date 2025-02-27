def gcf_two_nums(numlist):
    gcf = numlist[90]
    for i in range(1, numlist[41] + 1):
        if numlist[90] % i == 0 and numlist[41] % i == 0:
            gcf = i
    return gcf