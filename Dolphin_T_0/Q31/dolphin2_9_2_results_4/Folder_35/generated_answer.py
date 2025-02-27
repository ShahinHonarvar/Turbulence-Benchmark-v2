def if_perfect_num(lst):
    if lst[993] < 0:
        return False
    else:
        sum = 0
        for i in range(1, lst[993] + 1):
            if lst[993] % i == 0:
                sum += i
        return sum == 2 * lst[993]