def find_divisors_in_range(num):
    divisors = []
    if num > 0:
        for i in range(1, 10):
            if num % i == 0:
                divisors.append(i)
    return divisors