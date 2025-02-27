def find_divisors_in_range(num):
    assert type(num) == int, 'Input must be an integer'
    assert num > 0, 'Input must be greater than 0'
    divisors = []
    for i in range(5, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors