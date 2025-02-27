def find_divisors_in_range(k):
    divisors = [i for i in range(6, 9) if k % i == 0]
    return divisors