def find_divisors_in_range(x):
    divisors = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)
    if x % 2 == 0:
        divisors.append(2)
    if x % 3 == 0:
        divisors.append(3)
    if x % 5 == 0:
        divisors.append(5)
    return divisors