def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 50 <= i <= 84]
    if divisors:
        return divisors
    else:
        return []