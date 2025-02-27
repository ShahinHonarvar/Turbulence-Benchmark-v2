def sum_of_divisors_in_range(n):
    divisor_list = []
    for x in range(60, 87):
        if n % x == 0:
            divisor_list.append(x)
    return sum(divisor_list) if divisor_list else 0