def find_divisors_in_range(n):
    result = [i for i in range(3, 6) if n % i == 0]
    return result