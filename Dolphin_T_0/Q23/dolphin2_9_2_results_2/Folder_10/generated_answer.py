def find_divisors_in_range(x):
    divisors = []
    for i in range(int(x ** 0.5), 0, -1):
        if x % i == 0:
            if i >= 60 and i <= 86:
                divisors.append(i)
            if x // i >= 60 and x // i <= 86:
                divisors.append(x // i)
    return divisors