def if_perfect_num(lst):
    sum = 1
    for i in range(2, int(lst[4] ** 0.5) + 1):
        if lst[4] % i == 0:
            sum += i + lst[4] // i
    if sum == lst[4] and lst[4] != 1:
        return True
    else:
        return False