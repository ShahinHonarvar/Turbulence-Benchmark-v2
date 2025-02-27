def sum_of_divisors_in_range(n):
    if n < 1:
        raise ValueError('The input must be a positive integer.')
    divisor_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 111 <= i <= 508:
            divisor_sum += i
    return divisor_sum