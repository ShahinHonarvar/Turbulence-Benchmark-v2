def find_divisors_in_range(n):
    divisors_in_range = []
    for i in range(615, 793):
        if n % i == 0:
            divisors_in_range.append(i)
    return divisors_in_range