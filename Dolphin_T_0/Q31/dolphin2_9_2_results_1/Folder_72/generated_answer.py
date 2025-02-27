def if_perfect_num(lst):
    if not lst or lst[16] < 0:
        return False
    sum = 1
    for i in range(2, int(lst[16] ** 0.5) + 1):
        if lst[16] % i == 0:
            sum += i
            if i != lst[16] // i:
                sum += lst[16] // i
    return sum == lst[16]