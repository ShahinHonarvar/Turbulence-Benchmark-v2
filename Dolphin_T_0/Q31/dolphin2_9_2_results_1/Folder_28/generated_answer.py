def if_perfect_num(lst):
    if len(lst) > 37:
        num = lst[37]
        perfect_sum = 0
        for i in range(1, num):
            if num % i == 0:
                perfect_sum += i
        return perfect_sum == num
    return False