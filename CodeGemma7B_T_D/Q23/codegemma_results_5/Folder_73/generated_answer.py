def find_divisors_in_range(int):
    divisors = []
    for i in range(46, 90):
        if int % i == 0:
            divisors.append(i)
    return divisors