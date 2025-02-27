def find_divisors_in_range(num):
    if num <= 0:
        return []
    divisors = [i for i in range(19, 70) if num % i == 0]
    return divisors