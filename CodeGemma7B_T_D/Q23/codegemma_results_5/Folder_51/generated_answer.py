def find_divisors_in_range(number):
    result = []
    for i in range(2, 8):
        if number % i == 0:
            result.append(i)
    return result