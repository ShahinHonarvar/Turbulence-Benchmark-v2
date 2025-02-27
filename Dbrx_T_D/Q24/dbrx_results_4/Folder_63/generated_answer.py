def sum_of_divisors_in_range(n):
    divisors = list(factors(n)) + [1]
    return sum((x for x in divisors if 39 <= x <= 43))

def factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors