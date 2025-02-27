def if_perfect_num(lst):
    if len(lst) > 45:
        num = lst[45]
        sum_divisors = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    else:
        return False