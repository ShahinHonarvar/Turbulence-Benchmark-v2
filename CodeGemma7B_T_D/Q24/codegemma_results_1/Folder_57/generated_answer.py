def sum_of_divisors_in_range(num):
    divisor_list = []
    for divisor in range(15, 93):
        if num % divisor == 0:
            divisor_list.append(divisor)
    return sum(divisor_list) if divisor_list else 0