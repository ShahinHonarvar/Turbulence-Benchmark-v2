def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 50 <= i <= 81]
    if not divisors:
        return []
    return divisors