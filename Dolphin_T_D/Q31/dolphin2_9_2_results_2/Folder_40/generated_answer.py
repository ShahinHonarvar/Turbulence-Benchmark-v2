def if_perfect_num(lst):
    n = lst[7]
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if n // i == i:
                sum_divisors = sum_divisors + i
            else:
                sum_divisors = sum_divisors + (i + n // i)
            i += 1
    return sum_divisors == n