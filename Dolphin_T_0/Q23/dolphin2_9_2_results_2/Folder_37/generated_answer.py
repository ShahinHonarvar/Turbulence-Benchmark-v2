def find_divisors_in_range(num):
    divisors = []
    for i in range(3, 8):
        if num % i == 0:
            divisors.append(i)
    return divisors