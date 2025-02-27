def find_divisors_in_range(n):
    result = []
    for i in range(20, 51):
        if n % i == 0:
            result.append(i)
    return result