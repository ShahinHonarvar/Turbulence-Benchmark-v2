def find_divisors_in_range(x):
    divisors = [i for i in range(1, x + 1) if x % i == 0 and 615 <= i <= 792]
    return divisors