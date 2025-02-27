def if_perfect_num(lst):
    sum = 0
    for i in range(1, lst[990]):
        if lst[990] % i == 0:
            sum += i
    if sum == lst[990]:
        return True
    else:
        return False