def find_divisors_in_range(num):
    divisors = [i for i in list(range(14, 94)) if num % i == 0]
    return divisors if divisors else []