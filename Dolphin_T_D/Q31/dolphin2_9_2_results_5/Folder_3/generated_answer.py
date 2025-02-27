def if_perfect_num(list_of_integers):
    target_integer = list_of_integers[100]
    sum_of_divisors = 1
    i = 2
    while i * i <= target_integer:
        if target_integer % i:
            i += 1
        else:
            if target_integer // i == i:
                sum_of_divisors = sum_of_divisors + i
            else:
                sum_of_divisors = sum_of_divisors + i + target_integer // i
            i += 1
    return sum_of_divisors == target_integer