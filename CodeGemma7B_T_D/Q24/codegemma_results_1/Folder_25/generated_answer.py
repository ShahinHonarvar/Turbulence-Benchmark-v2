def sum_of_divisors_in_range(num):
    divisor_list = []
    for i in range(84, 86 + 1):
        if num % i == 0:
            divisor_list.append(i)
    if len(divisor_list) == 0:
        return 0
    else:
        return sum(divisor_list)