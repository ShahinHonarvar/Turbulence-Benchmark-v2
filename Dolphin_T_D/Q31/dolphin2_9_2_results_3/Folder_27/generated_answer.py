def if_perfect_num(lst):
    num = lst[55]
    sum_of_divisors = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    return num == sum_of_divisors