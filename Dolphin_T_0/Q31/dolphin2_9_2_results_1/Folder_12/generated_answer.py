def if_perfect_num(lst):
    if len(lst) < 28:
        return False
    else:
        num = lst[27]
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        if sum_divisors == num and num != 0:
            return True
        else:
            return False