def find_divisors_in_range(num):
    divisors = []
    for n in range(46, 66):
        if num % n == 0:
            divisors.append(n)
    return divisors or []