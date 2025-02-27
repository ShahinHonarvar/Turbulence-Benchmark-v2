def find_divisors_in_range(num):
    if isinstance(num, int) and num > 0:
        divisors = [i for i in range(1, 2 + 1) if num % i == 0]
        if len(divisors) > 0:
            return divisors
        else:
            return []
    else:
        raise ValueError('Invalid input. Please provide a positive integer.')