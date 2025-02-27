def find_divisors_in_range(num):
    assert num > 0, 'Number must be positive'
    divisors = []
    for i in range(6, 9 + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors