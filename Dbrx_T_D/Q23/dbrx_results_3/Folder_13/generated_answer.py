def find_divisors_in_range(n):
    divisors = []
    for i in range(472, 828):
        if i > n:
            break
        if n % i == 0:
            divisors.append(i)
    return divisors