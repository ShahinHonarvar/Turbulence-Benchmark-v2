def find_divisors_in_range(num):
    if num < 70 or num > 72:
        return []
    divisors = [i for i in range(70, 73) if num % i == 0]
    return divisors