def sum_of_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Input must be a positive integer')
    divisors = []
    for i in range(2, num + 1):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum((d for d in divisors if d in range(6, 9)))