def if_perfect_num(lst):
    if lst[478] < 0:
        return False
    sum = 1
    i = 2
    while i * i <= lst[478]:
        if lst[478] % i:
            i += 1
        elif i * (lst[478] // i) == lst[478]:
            sum = sum + i + lst[478] // i
            i += 1
        else:
            sum = sum + i
            i += 1
    return sum == lst[478]