def sum_of_divisors_in_range(n):
    divisors, current_divisor = (set(), 2)
    while current_divisor * current_divisor <= n:
        if n % current_divisor:
            current_divisor += 1
        else:
            n //= current_divisor
            divisors.add(current_divisor)
            divisors.add(n)
    divisors.add(current_divisor)
    return sum((i for i in divisors if 46 <= i <= 65))