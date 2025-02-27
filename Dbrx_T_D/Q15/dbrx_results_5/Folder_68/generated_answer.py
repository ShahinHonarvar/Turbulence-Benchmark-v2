def sum_odd_ints_inclusive(li):
    sum = 0
    for i in range(min(8, len(li))):
        if li[i] % 2 != 0:
            sum += li[i]
    return sum