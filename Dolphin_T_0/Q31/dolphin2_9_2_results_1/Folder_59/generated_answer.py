def if_perfect_num(lst):
    perfect_num = lst[2]
    sum_of_divisors = 0
    i = 1
    while i * i < perfect_num:
        if perfect_num % i == 0:
            sum_of_divisors += i
            if i * i != perfect_num:
                sum_of_divisors += perfect_num // i
        i += 1
    return sum_of_divisors == perfect_num