def sum_of_divisors_in_range(n):
    divisor_list = []
    for i in range(111, 509):
        if n % i == 0:
            divisor_list.append(i)
    if not divisor_list:
        return 0
    else:
        return sum(divisor_list)