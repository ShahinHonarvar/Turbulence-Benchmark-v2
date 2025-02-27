def find_divisors_in_range(num):
    if num <= 0:
        return []
    divisors = [i for i in range(45, 73) if num % i == 0]
    return divisors if divisors else []