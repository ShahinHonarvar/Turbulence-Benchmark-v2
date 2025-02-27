def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError('Input argument must be positive')
    sum_of_divisors = 0
    for i in range(658, 869):
        if n % i == 0 and i % n == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors