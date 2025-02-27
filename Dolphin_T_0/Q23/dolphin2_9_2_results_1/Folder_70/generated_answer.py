def find_divisors_in_range(number):
    result = []
    for i in range(586, 841):
        if number % i == 0:
            result.append(i)
    return result