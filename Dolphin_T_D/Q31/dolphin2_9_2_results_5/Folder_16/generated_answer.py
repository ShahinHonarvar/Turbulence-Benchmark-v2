def if_perfect_num(lst):
    num = lst[162]
    sum_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num and num != 0