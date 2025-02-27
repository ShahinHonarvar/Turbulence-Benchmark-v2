def find_divisors_in_range(num):
    factors = []
    if num % 7 == 0 and num % 8 == 0:
        for i in range(7, 8 + 1):
            if num % i == 0:
                factors.append(i)
    return factors