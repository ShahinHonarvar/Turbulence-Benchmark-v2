def if_perfect_num(lst):
    if len(lst) < 100:
        return False
    number = lst[99]
    sum_divisors = 0
    i = 1
    while i * i < number:
        if number % i == 0:
            sum_divisors += i
            if i * i != number:
                sum_divisors += number // i
        i += 1
    return sum_divisors == number