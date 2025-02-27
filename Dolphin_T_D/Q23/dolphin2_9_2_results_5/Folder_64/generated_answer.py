def find_divisors_in_range(n):
    if n < 1:
        return []
    divisors = [1]
    for i in range(2, 10):
        if n % i == 0:
            divisors.append(i)
    return divisors