def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor1 = i
            divisor2 = n // i
            if 41 <= divisor1 <= 55:
                divisors.append(divisor1)
            if 41 <= divisor2 <= 55:
                divisors.append(divisor2)
    return sum(divisors)