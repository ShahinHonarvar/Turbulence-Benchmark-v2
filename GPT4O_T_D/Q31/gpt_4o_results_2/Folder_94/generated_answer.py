def if_perfect_num(lst):
    if len(lst) <= 93:
        return False
    num = lst[93]
    if num < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num