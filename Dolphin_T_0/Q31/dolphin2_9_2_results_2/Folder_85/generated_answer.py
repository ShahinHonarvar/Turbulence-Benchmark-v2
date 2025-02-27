def if_perfect_num(lst):
    if len(lst) < 24:
        return False
    num = lst[23]
    if num <= 1:
        return False
    divisors_sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i == num / i:
                divisors_sum = divisors_sum + i
            else:
                divisors_sum = divisors_sum + (i + num // i)
            i += 1
    return divisors_sum == num