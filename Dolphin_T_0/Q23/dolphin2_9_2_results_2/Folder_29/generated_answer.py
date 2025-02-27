def find_divisors_in_range(num):
    divisors = [i for i in range(43, 78) if num % i == 0]
    return divisors