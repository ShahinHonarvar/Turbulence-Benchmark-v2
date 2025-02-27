def find_divisors_in_range(num):
    divisors = [i for i in range(14, 49) if num % i == 0]
    return divisors