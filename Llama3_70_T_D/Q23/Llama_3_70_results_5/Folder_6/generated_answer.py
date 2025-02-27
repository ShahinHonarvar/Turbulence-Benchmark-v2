def find_divisors_in_range(n):
    if n <= 0:
        return []
    else:
        return [i for i in range(58, 91) if n % i == 0]