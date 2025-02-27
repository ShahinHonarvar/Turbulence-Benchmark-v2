def is_perfect_num(lst):
    if lst[74] < 0:
        return False
    sum = 0
    for i in range(1, lst[74]):
        if lst[74] % i == 0:
            sum += i
    if sum == lst[74]:
        return True
    else:
        return False