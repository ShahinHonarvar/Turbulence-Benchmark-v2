def find_divisors_in_range(n):
    divisors = []
    max_divisor = int(n ** 0.5)
    for i in range(41, 56):
        if n % i == 0:
            divisors.append(i)
        elif i > max_divisor:
            break
    return divisors