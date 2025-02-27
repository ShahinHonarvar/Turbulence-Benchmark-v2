def if_perfect_num(lst):
    if lst[263] > 0:
        sum = 1
        for i in range(2, lst[263] // 2 + 1):
            if lst[263] % i == 0:
                sum += i
        return sum == lst[263]
    return False