def sum_of_divisors_in_range(n):
    if n <= 0 or n % 2 == 0:
        return 0
    divisor_list = []
    for i in range(2, (n + 1) // 2 + 1):
        if n % i == 0:
            divisor_list.append(i)
            divisor_list.append(n // i)
    divisor_sum = 0
    for divisor in divisor_list:
        if 10 <= divisor <= 55:
            divisor_sum += divisor
    return divisor_sum if divisor_sum != 0 else 0