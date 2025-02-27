def find_divisors_in_range(n):
    divisors = []
    for i in range(615, 793):
        if i % n == 0:
            divisors.append(i)
    return divisors