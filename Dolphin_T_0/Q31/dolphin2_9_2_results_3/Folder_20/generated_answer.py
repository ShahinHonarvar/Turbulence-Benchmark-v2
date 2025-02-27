def if_perfect_num(lst):
    if len(lst) < 54:
        return False
    num = lst[53]
    sum_of_divisors = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum_of_divisors += i
            if i * i != num:
                sum_of_divisors += num // i
        i += 1
    return sum_of_divisors == num